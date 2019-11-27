import pytest

from gomoku import board

def test_is_won_1():
    chess = board.Gomoku(board_size=6)

    chess.status=[0,0,0,1,0,0,
                  0,0,0,1,0,0,
                  0,0,0,1,0,0,
                  0,0,0,1,0,0,
                  0,0,0,1,0,0,
                  0,0,0,0,0,0]
    chess.last_action = 3
    assert chess.is_won()==True
    chess.last_action = 9
    assert chess.is_won()==True
    chess.last_action = 15
    assert chess.is_won()==True
    chess.last_action = 21
    assert chess.is_won()==True
    chess.last_action = 27
    assert chess.is_won()==True


def test_is_won_2():
    chess = board.Gomoku(board_size=6)

    chess.status=[0,0,0,0,0,0,
                  0,0,0,0,2,0,
                  0,0,0,0,2,0,
                  0,0,0,0,2,0,
                  0,0,0,0,2,0,
                  0,0,0,0,2,0]
    chess.last_action = 34        #error
    assert chess.is_won()==True
    chess.last_action = 28
    assert chess.is_won()==True
    chess.last_action = 22
    assert chess.is_won()==True
    chess.last_action = 16
    assert chess.is_won()==True
    chess.last_action = 10
    assert chess.is_won()==True

def test_is_won_3():
    chess = board.Gomoku(board_size=6)

    chess.status=[0,0,0,0,0,0,
                  0,1,0,0,0,0,
                  0,0,1,0,0,0,
                  0,0,0,1,0,0,
                  0,0,0,0,1,0,
                  0,0,0,0,0,1]
    chess.last_action = 7         #error    
    assert chess.is_won()==True
    chess.last_action = 14
    assert chess.is_won()==True
    chess.last_action = 21
    assert chess.is_won()==True
    chess.last_action = 28
    assert chess.is_won()==True
    chess.last_action = 35
    assert chess.is_won()==True

def test_is_won_4():
    chess = board.Gomoku(board_size=6)

    chess.status=[0,0,0,0,0,0,
                  0,0,0,0,0,1,
                  0,0,0,0,1,0,
                  0,0,0,1,0,0,
                  0,0,1,0,0,0,
                  0,1,0,0,0,0]
    chess.last_action = 11
    assert chess.is_won()==True
    chess.last_action = 16
    assert chess.is_won()==True
    chess.last_action = 21
    assert chess.is_won()==True
    chess.last_action = 26
    assert chess.is_won()==True
    chess.last_action = 31
    assert chess.is_won()==True
