import datetime
from mcts import *
import random
from expert import get_max_value_pos


class Player(object):
    def __init__(self):
        pass

    def get_action(self):
        pass
    
class HumanPlayer(Player):
    def __init__(self,board):
    	self.board=board

    
    def get_action(self):
    	while True:
    		n=raw_input("please enter actionition:")
        	ret = n.split(',')
        	if len(ret)==2:
        		x=int(ret[0])
        		y=int(ret[1])
        		if x>=0 and x<9 and y>=0 and y<9:
        			if self.board.status[x*9+y]=='-':
        				break
        	print("invalid input")
        action =x*9+y
        return action


class MCTSPlayer(Player):
    """AI player based on MCTS"""
    def __init__(self,board,c_puct=5,simulate_time=5):
        self.mcts = MCTS(policy_value_fn, c_puct, simulate_time)
        self.board=board

    def reset_player(self):
        self.mcts.update_with_move(-1)


    
    def get_action(self):
        sensible_moves = self.board.available
        if len(sensible_moves) > 0:
            action = self.mcts.get_move(self.board)
            self.mcts.update_with_move(-1)
            return action

        else:
            print("WARNING: the board is full")

    def __str__(self):
        return "MCTS "

class RandomPlayer(Player):
	def __init__(self,board):
		self.board=board

	def get_action(self):
			return random.choice(self.board.available)




class ESTPlayer(Player):
    def __init__(self,board):
        self.board=board

    def get_action(self):
        x,y=get_max_value_pos(self.board.status)
        action=x*9+y
        return action



