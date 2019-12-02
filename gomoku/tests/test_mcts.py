import pytest

from gomoku import board,player,mcts

def test_mcts_get_move1():

    chess = board.Gomoku(board_size=6)
    chess.last_action  = 1
    chess.moved_player = 2
    chess.status =[ 
              0,2,0,0,0,2,
              1,1,1,1,0,0,
              0,0,0,0,0,2,
              2,0,0,0,0,0,
              0,0,0,0,0,0,
              0,2,0,0,0,0]
    for action in range(chess.size*chess.size):
        if chess.status[action] !=0:
            chess.available.remove(action)

    chess.current_player = 1          
    mcts_app = mcts.MCTS( mcts.policy_value_fn, c_puct=5, simulate_time=5)         
   
    count = 0
    for i in range(4):
        move= mcts_app.get_move(chess)
        if move == 10:
            count = count + 1

    assert count >= 2  #4次超过2次

''' 
def test_mcts_get_move2():

    chess = board.Gomoku(board_size=6)
    chess.last_action  = 1
    chess.moved_player = 2
    chess.status =[ 
              0,2,0,0,0,2,
              0,1,1,1,0,0,
              0,0,0,0,0,2,
              2,0,0,0,0,0,
              0,0,0,0,0,0,
              0,0,0,0,0,0]
    for action in range(chess.size*chess.size):
        if chess.status[action] !=0:
            chess.available.remove(action)

    chess.current_player = 1          
    mcts_app = mcts.MCTS( mcts.policy_value_fn, c_puct=5, simulate_time=20)         

    move= mcts_app.get_move(chess)

    assert move==6 or move == 10
'''    

