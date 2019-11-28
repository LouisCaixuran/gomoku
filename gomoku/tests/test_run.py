import pytest

from gomoku import board,player

def test_expert_vs_random():
    chess = board.Gomoku(board_size=6)
    player1 =  player.RandomPlayer(chess)
    player2 =  player.ExpertPlayer(chess)
    chess.play(player1,player2, isShow=False)
    
    assert chess.end == True
    assert chess.winner == chess.player2

    
def test_mcts_vs_expert():
    chess = board.Gomoku(board_size=6)
    player1 =  player.MCTSPlayer(chess,simulate_time=0.1)
    player2 =  player.ExpertPlayer(chess)
    chess.play(player1,player2, isShow=False)
    
    assert chess.end == True
    assert chess.winner == chess.player2

