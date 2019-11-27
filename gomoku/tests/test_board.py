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
    chess.current_player = 1
    assert chess.is_won()==True


def test_is_won_2():
    chess = board.Gomoku(board_size=6)

    chess.current_player = 2
    chess.last_action = 10
    chess.status=[0,0,0,0,0,0,
                  0,0,0,0,2,0,
                  0,0,0,0,2,0,
                  0,0,0,0,2,0,
                  0,0,0,0,2,0,
                  0,0,0,0,2,0]
    assert chess.is_won()==True

def test_is_won_3():
    chess = board.Gomoku(board_size=6)

    chess.last_action = 7
    chess.current_player = 1
    chess.status=[0,0,0,0,0,0,
                  0,1,0,0,0,0,
                  0,0,1,0,0,0,
                  0,0,0,1,0,0,
                  0,0,0,0,1,0,
                  0,0,0,0,0,1]
    assert chess.is_won()==True

def test_is_won_4():
    chess = board.Gomoku(board_size=6)

    chess.last_action = 11
    chess.current_player = 1
    chess.status=[0,0,0,0,0,0,
                  0,0,0,0,0,1,
                  0,0,0,0,1,0,
                  0,0,0,1,0,0,
                  0,0,1,0,0,0,
                  0,1,0,0,0,0]
    assert chess.is_won()==True


def test_is_won_5():
    chess = board.Gomoku(board_size=6)

    chess.last_action = 11
    chess.current_player = 1
    chess.status=[0,0,0,0,0,0,
                  0,0,0,0,0,1,
                  0,0,0,0,1,0,
                  0,0,0,1,0,0,
                  0,0,2,0,0,0,
                  0,1,0,0,0,0]
    assert chess.is_won()==False


def test_is_won_6():
    chess = board.Gomoku(board_size=6)

    chess.last_action = 11
    chess.current_player = 1
    chess.status=[0,0,0,0,0,0,
                  0,0,0,0,0,1,
                  0,0,0,0,1,0,
                  0,0,0,0,0,0,
                  0,1,1,1,1,1,
                  0,1,0,0,0,0]
    assert chess.is_won()==True
    
