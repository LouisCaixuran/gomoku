
from gomoku import board, player


def test_expert_vs_random():
    chess = board.Gomoku(board_size=6)
    player1 = player.RandomPlayer(chess)
    player2 = player.ExpertPlayer(chess)
    chess.play(player1, player2, isShow=False)

    assert chess.end
    assert chess.winner == chess.player2


def test_mcts_vs_expert():
    chess = board.Gomoku(board_size=6)
    player1 = player.MCTSPlayer(chess, simulate_time=1)
    player2 = player.ExpertPlayer(chess)
    chess.play(player1, player2, isShow=False)

    assert chess.end
    assert chess.winner != chess.player1  # tie or expert win


def test_mcts_vs_mcts():
    chess = board.Gomoku(board_size=6)
    player1 = player.MCTSPlayer(chess, simulate_time=1)
    player2 = player.RandomPlayer(chess)
    chess.play(player1, player2, isShow=False)

    assert chess.end
    assert chess.winner != chess.player2  # tie or mcts win
