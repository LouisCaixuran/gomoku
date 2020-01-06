import numpy as np
# import pytest
from gomoku import board


def test_is_won_1():
    chess = board.Gomoku(board_size=6)

    chess.status = [0, 0, 0, 1, 0, 0,
                    0, 0, 0, 1, 0, 0,
                    0, 0, 0, 1, 0, 0,
                    0, 0, 0, 1, 0, 0,
                    0, 0, 0, 1, 0, 0,
                    0, 0, 0, 0, 0, 0]
    chess.last_action = 3
    chess.moved_player = 1
    assert chess.is_won()


def test_is_won_2():
    chess = board.Gomoku(board_size=6)

    chess.moved_player = 2
    chess.last_action = 10
    chess.status = [0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 2, 0,
                    0, 0, 0, 0, 2, 0,
                    0, 0, 0, 0, 2, 0,
                    0, 0, 0, 0, 2, 0,
                    0, 0, 0, 0, 2, 0]
    assert chess.is_won()


def test_is_won_3():
    chess = board.Gomoku(board_size=6)

    chess.last_action = 7
    chess.moved_player = 1
    chess.status = [0, 0, 0, 0, 0, 0,
                    0, 1, 0, 0, 0, 0,
                    0, 0, 1, 0, 0, 0,
                    0, 0, 0, 1, 0, 0,
                    0, 0, 0, 0, 1, 0,
                    0, 0, 0, 0, 0, 1]
    assert chess.is_won()


def test_is_won_4():
    chess = board.Gomoku(board_size=6)

    chess.last_action = 11
    chess.moved_player = 1
    chess.status = [0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 1,
                    0, 0, 0, 0, 1, 0,
                    0, 0, 0, 1, 0, 0,
                    0, 0, 1, 0, 0, 0,
                    0, 1, 0, 0, 0, 0]
    assert chess.is_won()


def test_is_won_5():
    chess = board.Gomoku(board_size=6)

    chess.last_action = 11
    chess.moved_player = 1

    chess.status = [0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 1,
                    0, 0, 0, 0, 1, 0,
                    0, 0, 0, 1, 0, 0,
                    0, 0, 2, 0, 0, 0,
                    0, 1, 0, 0, 0, 0]
    assert not chess.is_won()


def test_is_won_6():
    chess = board.Gomoku(board_size=6)

    chess.last_action = 11
    chess.moved_player = 1
    chess.status = [0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 1,
                    0, 0, 0, 0, 1, 0,
                    0, 0, 0, 0, 0, 0,
                    0, 1, 1, 1, 1, 1,
                    0, 1, 0, 0, 0, 0]
    assert chess.is_won()


def test_current_state_1():
    chess = board.Gomoku(board_size=3)

    chess.last_action = 2
    chess.moved_player = 1
    chess.current_player = 2
    chess.status = [1, 2, 1,
                    0, 0, 0,
                    0, 0, 0]

    state = chess.current_state()

    p = np.zeros((4, 3, 3))
    p[0][0, 0] = 1
    p[0][0, 2] = 1

    p[1][0, 1] = 1

    p[2][0, 2] = 1

    p[3] = 0

    assert (state == p).all()  # 所有元素相等，返回true
