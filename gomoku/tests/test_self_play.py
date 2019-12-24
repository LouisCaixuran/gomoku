from gomoku import board,self_play
import numpy as np


class MockPlayer(object):

    def __init__(self,board,is_selfplay=0):
        self.board = board
        pass

    def get_action(self, return_prob=0):
        probs= np.zeros(self.board.width*self.board.height)
        probs[0]=1
        move = 0
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
    value = 1
    state[0][0,0]=1
    state[2][0,0]=1
    state[3]=1
    probs[0]=1
    s.append(state)
    p.append(probs)
    v.append(value)
    
    result =list(zip(s,p,v))

    a = self_play.start_self_play(chess,player)
    
    print(list(a)[0][2])
    print(result[0][2])
    assert result == list(a)


     


