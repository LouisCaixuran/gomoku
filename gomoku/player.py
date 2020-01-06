# import datetime
from gomoku.mcts import MCTS, policy_value_fn
import random
from gomoku.expert import Expert


class Player(object):
    def __init__(self):
        pass

    def get_action(self):
        pass

    def reply(self, x, y):
        pass


class HumanPlayer(Player):
    def __init__(self, board):
        self.board = board

    def get_action(self):
        while True:
            n = input("please enter action:")
            ret = n.split(',')
            if len(ret) == 2:
                x = int(ret[0])
                y = int(ret[1])
                if x >= 0 and x < self.board.width and y >= 0 \
                   and y < self.board.width:
                    if self.board.status[x * self.board.width + y] == 0:
                        break
            print("invalid input")
        action = x * self.board.width + y
        return action


class MCTSPlayer(Player):
    """AI player based on MCTS"""

    def __init__(self, board, c_puct=5, simulate_time=5):
        self.mcts = MCTS(policy_value_fn, c_puct, simulate_time)
        self.board = board

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
    def __init__(self, board):
        self.board = board

    def get_action(self):
        return random.choice(self.board.available)


class ExpertPlayer(Player):
    """AI player based on Expert"""

    def __init__(self, board):
        self.expert = Expert()
        self.board = board

    def get_action(self):
        sensible_moves = self.board.available
        if len(sensible_moves) > 0:
            move = self.expert.get_move(self.board)
            return move
        else:
            print("WARNING: the board is full")

    def __str__(self):
        return "Expert"
