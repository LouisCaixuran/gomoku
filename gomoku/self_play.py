from board import Gomoku
from mcts import *
def start_self_play(Gomoku):
	states=Gomoku.current_state()
	mcts = MCTS(policy_value_fn, 5)
	mctd._policy
