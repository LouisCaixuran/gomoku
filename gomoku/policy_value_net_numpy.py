# -*- coding: utf-8 -*-
"""
Implement the policy value network using numpy, so that we can play with the
trained AI model without installing any DL framwork
"""

from __future__ import print_function
import numpy as np
import pickle
from collections import OrderedDict
import copy


def sigmoid(x):
    return 1 / (1 + np.exp(-x))    

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T 

    x = x - np.max(x) 
    return np.exp(x) / np.sum(np.exp(x))

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    if t.size == y.size:
        t = t.argmax(axis=1)
             
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


def im2col(input_data, filter_h, filter_w, stride=1, pad=0):

    N, C, H, W = input_data.shape
    out_h = (H + 2*pad - filter_h)//stride + 1
    out_w = (W + 2*pad - filter_w)//stride + 1

    img = np.pad(input_data, [(0,0), (0,0), (pad, pad), (pad, pad)], 'constant')
    col = np.zeros((N, C, filter_h, filter_w, out_h, out_w))

    for y in range(filter_h):
        y_max = y + stride*out_h
        for x in range(filter_w):
            x_max = x + stride*out_w
            col[:, :, y, x, :, :] = img[:, :, y:y_max:stride, x:x_max:stride]

    col = col.transpose(0, 4, 5, 1, 2, 3).reshape(N*out_h*out_w, -1)
    return col

def col2im(col, input_shape, filter_h, filter_w, stride=1, pad=0):
    N, C, H, W = input_shape
    out_h = (H + 2*pad - filter_h)//stride + 1
    out_w = (W + 2*pad - filter_w)//stride + 1
    col = col.reshape(N, out_h, out_w, C, filter_h, filter_w).transpose(0, 3, 4, 5, 1, 2)

    img = np.zeros((N, C, H + 2*pad + stride - 1, W + 2*pad + stride - 1))
    for y in range(filter_h):
        y_max = y + stride*out_h
        for x in range(filter_w):
            x_max = x + stride*out_w
            img[:, :, y:y_max:stride, x:x_max:stride] += col[:, :, y, x, :, :]

    return img[:, :, pad:H + pad, pad:W + pad]


class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        
        self.mask = (x <= 0)
        
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx


class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = sigmoid(x)
        self.out = out
        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out

        return dx

class Tanh:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = tanh(x)      #(np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x)) 
        self.out = out
        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out * self.out)

        return dx

class Affine:
    def __init__(self, W, b):
        self.W =W
        self.b = b
        
        self.x = None
        self.original_x_shape = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.original_x_shape = x.shape
        x = x.reshape(x.shape[0], -1)
        self.x = x

        out = np.dot(self.x, self.W) + self.b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)
        
        dx = dx.reshape(*self.original_x_shape)  
        return dx

class TanhMeanSquaredWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None 
        self.t = None 

    def forward(self, x, t):
        self.t = t
        self.tanh = Tanh()
        self.y = self.tanh.forward(x)
        self.loss = mean_squared_error(self.y, self.t)
        
        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        if self.t.size == self.y.size:
            dx = (self.y - self.t) / batch_size
        else:
            dx = self.y.copy()
            dx[np.arange(batch_size), self.t] -= 1
            dx = dx / batch_size
    
        dx = self.tanh.backward(dx)

        return dx

class MeanSquaredWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None 
        self.t = None 

    def forward(self, x, t):
        self.t = t
        self.y = x
        self.loss = mean_squared_error(self.y, self.t)
        
        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        if self.t.size == self.y.size:
            dx = (self.y - self.t) / batch_size
        else:
            dx = self.y.copy()
            dx[np.arange(batch_size), self.t] -= 1
            dx = dx / batch_size
        
        return dx

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None 
        self.t = None 

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        
        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        if self.t.size == self.y.size:
            dx = (self.y - self.t) / batch_size
        else:
            dx = self.y.copy()
            dx[np.arange(batch_size), self.t] -= 1
            dx = dx / batch_size
        
        return dx

class Convolution:
    def __init__(self, W, b, stride=1, pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad
        
        self.x = None   
        self.col = None
        self.col_W = None
        
        self.dW = None
        self.db = None

    def forward(self, x):
        FN, C, FH, FW = self.W.shape
        N, C, H, W = x.shape
        out_h = 1 + int((H + 2*self.pad - FH) / self.stride)
        out_w = 1 + int((W + 2*self.pad - FW) / self.stride)

        col = im2col(x, FH, FW, self.stride, self.pad)
        col_W = self.W.reshape(FN, -1).T

        out = np.dot(col, col_W) + self.b
        out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)

        self.x = x
        self.col = col
        self.col_W = col_W

        return out

    def backward(self, dout):
        FN, C, FH, FW = self.W.shape
        dout = dout.transpose(0,2,3,1).reshape(-1, FN)

        self.db = np.sum(dout, axis=0)
        self.dW = np.dot(self.col.T, dout)
        self.dW = self.dW.transpose(1, 0).reshape(FN, C, FH, FW)

        dcol = np.dot(dout, self.col_W.T)
        dx = col2im(dcol, self.x.shape, FH, FW, self.stride, self.pad)

        return dx


class Pooling:
    def __init__(self, pool_h, pool_w, stride=1, pad=0):
        self.pool_h = pool_h
        self.pool_w = pool_w
        self.stride = stride
        self.pad = pad
        
        self.x = None
        self.arg_max = None

    def forward(self, x):
        N, C, H, W = x.shape
        out_h = int(1 + (H - self.pool_h) / self.stride)
        out_w = int(1 + (W - self.pool_w) / self.stride)

        col = im2col(x, self.pool_h, self.pool_w, self.stride, self.pad)
        col = col.reshape(-1, self.pool_h*self.pool_w)

        arg_max = np.argmax(col, axis=1)
        out = np.max(col, axis=1)
        out = out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)

        self.x = x
        self.arg_max = arg_max

        return out

    def backward(self, dout):
        dout = dout.transpose(0, 2, 3, 1)
        
        pool_size = self.pool_h * self.pool_w
        dmax = np.zeros((dout.size, pool_size))
        dmax[np.arange(self.arg_max.size), self.arg_max.flatten()] = dout.flatten()
        dmax = dmax.reshape(dout.shape + (pool_size,)) 
        
        dcol = dmax.reshape(dmax.shape[0] * dmax.shape[1] * dmax.shape[2], -1)
        dx = col2im(dcol, self.x.shape, self.pool_h, self.pool_w, self.stride, self.pad)
        
        return dx


"""
   conv - relu - conv - relu - affine - relu - affine - softmax
   conv - relu - conv - relu - affine - relu - affine - tanh
 
"""
class DeepConvNet():
    def __init__(self, input_dim=(4, 64, 64),
                 conv_param_1 = {'filter_num':32, 'filter_size':3, 'pad':1, 'stride':1},
                 conv_param_2 = {'filter_num':64, 'filter_size':3, 'pad':1, 'stride':1},
                 conv_param_3 = {'filter_num':128, 'filter_size':3, 'pad':1, 'stride':1},
                 hidden_size = 256, output_size=64, last_layer = SoftmaxWithLoss() ):

        pre_node_nums = np.array([1*3*3, 16*3*3, 16*3*3, 32*3*3, hidden_size])
        weight_init_scales = np.sqrt(2.0 / pre_node_nums)  

        self.params = {}
        pre_channel_num = input_dim[0]
        for idx, conv_param in enumerate([conv_param_1, conv_param_2, conv_param_3]):
            self.params['W' + str(idx+1)] = weight_init_scales[idx] * np.random.randn(conv_param['filter_num'], pre_channel_num, conv_param['filter_size'], conv_param['filter_size'])
            self.params['b' + str(idx+1)] = np.zeros(conv_param['filter_num'])
            pre_channel_num = conv_param['filter_num']
        self.params['W4'] = weight_init_scales[3] * np.random.randn(128*8*8, hidden_size)
        self.params['b4'] = np.zeros(hidden_size)
        self.params['W5'] = weight_init_scales[4] * np.random.randn(hidden_size, output_size)
        self.params['b5'] = np.zeros(output_size)

        self.layers = []
        self.layers.append(Convolution(self.params['W1'], self.params['b1'], 
                           conv_param_1['stride'], conv_param_1['pad']))
        self.layers.append(Relu())
        self.layers.append(Convolution(self.params['W2'], self.params['b2'], 
                           conv_param_2['stride'], conv_param_2['pad']))
        self.layers.append(Relu())
        self.layers.append(Convolution(self.params['W3'], self.params['b3'], 
                           conv_param_3['stride'], conv_param_3['pad']))
        self.layers.append(Relu())
        self.layers.append(Affine(self.params['W4'], self.params['b4']))
        self.layers.append(Relu())
        #self.layers.append(Dropout(0.5))
        self.layers.append(Affine(self.params['W5'], self.params['b5']))
        #self.layers.append(Dropout(0.5))
        
        self.last_layer = last_layer       # default is  SoftmaxWithLoss()


    def predict(self, x, train_flg=False):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def loss(self, x, t):
        y = self.predict(x, train_flg=True)
        return self.last_layer.forward(y, t)

    def accuracy(self, x, t, batch_size=100):
        if t.ndim != 1 : t = np.argmax(t, axis=1)

        acc = 0.0

        for i in range(int(x.shape[0] / batch_size)):
            tx = x[i*batch_size:(i+1)*batch_size]
            tt = t[i*batch_size:(i+1)*batch_size]
            y = self.predict(tx, train_flg=False)
            y = np.argmax(y, axis=1)
            acc += np.sum(y == tt)

        return acc / x.shape[0]

    def gradient(self, x, t):
        # forward
        self.loss(x, t)

        # backward
        dout = 1
        dout = self.last_layer.backward(dout)

        tmp_layers = copy.copy(self.layers)        
        tmp_layers.reverse()
        for layer in tmp_layers:
            dout = layer.backward(dout)

        grads = {}
        for i, layer_idx in enumerate((0, 2, 4, 6, 8)):
            grads['W' + str(i+1)] = self.layers[layer_idx].dW
            grads['b' + str(i+1)] = self.layers[layer_idx].db

        return grads



class PolicyValueNet():
    def __init__(self, board_width=8, board_height=8, model_file=None):
        
        self.board_width = board_width
        self.board_height = board_height

        self.network_probs = DeepConvNet( input_dim=(4, board_width, board_height),
            conv_param_1 = {'filter_num':32, 'filter_size':3, 'pad':1, 'stride':1},
            conv_param_2 = {'filter_num':64, 'filter_size':3, 'pad':1, 'stride':1},
            conv_param_3 = {'filter_num':128, 'filter_size':3, 'pad':1, 'stride':1},
            hidden_size = 256, output_size= board_width*board_height, 
            last_layer = SoftmaxWithLoss() )

        self.network_value = DeepConvNet( input_dim=(4, board_width, board_height),
            conv_param_1 = {'filter_num':32, 'filter_size':3, 'pad':1, 'stride':1},
            conv_param_2 = {'filter_num':64, 'filter_size':3, 'pad':1, 'stride':1},
            conv_param_3 = {'filter_num':128, 'filter_size':3, 'pad':1, 'stride':1},
            hidden_size = 256, output_size = 1,
            last_layer= TanhMeanSquaredWithLoss())

        if model_file is not None:
            self.load_model(model_file)

    def policy_value_fn(self, board):
        legal_positions = board.availables
        current_state = board.current_state()
        x = current_state.reshape(-1, 4, self.board_width, self.board_height)
        
        probs = softmax(self.network_probs.predict(x))
        
        act_probs = zip(legal_positions, probs.flatten()[legal_positions])

        act_value = tanh(self.network_value.predict(x))
        
        return act_probs,act_value

    def policy_value(self, x):
        x = np.reshape(x,(-1,4,self.board_width, self.board_height))
        probs = self.network_probs.predict(x)
        value = self.network_value.predict(x)
        return sotfmax(probs), tanh(value)

    def train_step(self, state_batch, probs_batch, winner_batch, lr):
        state_batch = np.reshape(state_batch,(-1,4,self.board_width, self.board_height))
        probs_batch = np.reshape(probs_batch, (-1, self.board_width*self.board_height))
        winner_batch = np.reshape(winner_batch, (-1))

        grads_p = self.network_probs.gradient(state_batch,probs_batch)
        loss_p  = self.network_probs.loss(state_batch,probs_batch)
        for key in self.network_probs.params.keys():
            self.network_probs.params[key] -= lr*grads_p[key] 

        grads_v = self.network_value.gradient(state_batch,winner_batch)
        loss_v  = self.network_value.loss(state_batch,winner_batch)
        for key in self.network_value.params.keys():
            self.network_value.params[key] -= lr*grads_v[key] 

        return loss_p, loss_v
    
    def save_model(self, model_name="params.pkl"):
        params = {}
        params['network_probs'] = {} 
        params['network_value'] = {} 

        for key, val in self.network_probs.params.items():
            params['network_probs'][key] = val
        for key, val in self.network_value.params.items():
            params['network_value'][key] = val

        with open(model_name, 'wb') as f:
            pickle.dump(params, f)

    def load_model(self, model_name="params.pkl"):
        with open(model_name, 'rb') as f:
            params = pickle.load(f)
        
        for key, val in params['network_probs'].items():
            self.network_probs.params[key] = val

        for key, val in params['network_value'].items():
            self.network_value.params[key] = val

        for i, layer_idx in enumerate((0, 2, 4, 6, 8)):
            self.network_value.layers[layer_idx].W = self.network_value.params['W' + str(i+1)]
            self.network_value.layers[layer_idx].b = self.network_value.params['b' + str(i+1)]
            self.network_probs.layers[layer_idx].W = self.network_probs.params['W' + str(i+1)]
            self.network_probs.layers[layer_idx].b = self.network_probs.params['b' + str(i+1)]

if __name__ == '__main__':
    net = PolicyValueNet(8,8)
    net.save_model()
    net.load_model()
