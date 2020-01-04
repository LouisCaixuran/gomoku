import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import torch

import torch.optim as optim

    
class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1=nn.Conv2d(4,32,3,padding=1)
        self.conv2=nn.Conv2d(32,64,3,padding=1)
        self.conv3=nn.Conv2d(64,128,3,padding=1)

        self.p_fc1=nn.Conv2d(128,4,1)
        self.p_fc2=nn.Linear(4*8*8,64)

        self.v_fc1=nn.Conv2d(128,2,1)
        self.v_fc2=nn.Linear(2*8*8,1)

    def forward(self,x):
        a1=F.relu(self.conv1(x))
        a2=F.relu(self.conv2(a1))
        a3=F.relu(self.conv3(a2))

        p1=F.relu(self.p_fc1(a3))
        p_act = p1.view(-1, 4*8*8)

        p_out=F.softmax(self.p_fc2(p_act),dim=0)

        v1=F.relu(self.v_fc1(a3))
        v_act = v1.view(-1, 2*8*8)

        v_out=torch.tanh(self.v_fc2(v_act))
            

        return p_out,v_out

class PolicyValueNet():
    def __init__(self, board_width=8, board_height=8, model_file=None):
        
        self.board_width = board_width
        self.board_height = board_height
        self.model=Net()
        self.v_loss = nn.MSELoss()
        #self.p_loss=nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.01)
        if model_file:
            self.model.load_state_dict(torch.load(model_file))

    def policy_value_fn(self, board):
        legal_positions = board.available
        current_state = board.current_state()
        x = torch.FloatTensor(current_state.reshape(-1, 4, self.board_width, self.board_height))

        probs,value = self.model.forward(x)
        probs=probs.data.numpy()
        value=value.data.numpy()

        probs = zip(legal_positions, probs.flatten()[legal_positions])
        
        return probs,value

    def policy_value(self, x):
        x = torch.FloatTensor(np.reshape(x,(-1,4,self.board_width, self.board_height)))
        probs,value = self.model.forward(x)
        probs=probs.data.numpy()
        value=value.data.numpy()
        return probs, value

    def train_step(self, state_batch, probs_batch, winner_batch, lr):
    
        state_batch=torch.FloatTensor(state_batch)
        probs_batch=torch.LongTensor(probs_batch)
        winner_batch=torch.FloatTensor(winner_batch)

        self.optimizer.zero_grad()
        p_out,v_out = self.model(state_batch)
        p_loss = -torch.mean(torch.sum(probs_batch*torch.log(p_out), 1))
        v_loss=self.v_loss(v_out,winner_batch)
        loss=p_loss+v_loss
        loss.backward()
        self.optimizer.step()

        return p_loss.item(),v_loss.item()

    def save_model(self,dir):
        torch.save(self.model.state_dict(),dir)


if __name__ == '__main__':
    net=PolicyValueNet()
    net.save_model("./testmodel")

