from gomoku import board,self_play
import numpy as np


class MockPlayer(object):

    def __init__(self,board,is_selfplay=0):
        self.board = board
        pass

    def get_action(self, return_prob=0):
        probs= np.zeros(self.board.width*self.board.height)
        move = self.board.available[0]
        probs[move]=0.9
        #move = 0
        return move, probs

    def reset_player(self):
        pass
    

def test_start_self_play():
    chess = board.Gomoku(board_size=2,n_long=1)
    player = MockPlayer(chess)
    
    s=[]
    p=[]
    v=[]
    
    state = np.zeros((4,2,2))
    probs = np.zeros((2*2))
    
    value=1.0
    state[3]=1.0
    
    probs[0]=0.9

    s.append(state)
    p.append(probs)
    v.append(value)
    
    result = list(zip(s,p,v))

    a = self_play.start_self_play(chess,player)
    
    b=list(a)

    for i in range(len(b)):
       assert (b[i][0]==result[i][0]).all()
       assert  (b[i][1]==result[i][1]).all()
       assert  b[i][2]==result[i][2]
        
     

def test_start_self_play_1():
    chess = board.Gomoku(board_size=2,n_long=2)
    player = MockPlayer(chess)
    
    s=[]
    p=[]
    v=[]
    
    state = np.zeros((4,2,2))
    probs = np.zeros((2*2))
    
    state[3]=1.0
    probs[0]=0.9
    value = 1.0
    s.append(state)
    p.append(probs)
    v.append(value)
   
   
    state = np.zeros((4,2,2))
    probs = np.zeros((2*2))
    state[0][0,0]=1.0
    state[2][0,0]=1.0
    probs[1] = 0.9
    value =-1.0
    s.append(state)
    p.append(probs)
    v.append(value)

   
    state = np.zeros((4,2,2))
    probs = np.zeros((2*2))
   
    state[0][0,0]=1.0
    state[1][0,1]=1.0
    state[2][0,1]=1.0
    state[3] =1.0 

    probs[2] =0.9
    value = 1.0

    s.append(state)
    p.append(probs)
    v.append(value)

    result = list(zip(s,p,v))

    a = self_play.start_self_play(chess,player)
    
    b=list(a)

    for i in range(len(b)):
        assert (b[i][0]==result[i][0]).all()
        assert (b[i][1]==result[i][1]).all()
        assert b[i][2]==result[i][2]

