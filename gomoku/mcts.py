# encoding: utf-8
import numpy as np
import copy
from operator import itemgetter
import datetime


def rollout_policy_fn(board):
    action_probs = np.random.rand(len(board.available))
    return zip(board.available, action_probs)


def policy_value_fn(board):
    """a function that takes in a board and outputs a list of
    (action, probability) tuples and a score for the board"""
    # return uniform probabilities and 0 score for pure MCTS
    probs = np.ones(len(board.available)) / len(board.available)
    # probs = np.random.random(len(board.available))
    # max_action = board.available[int(np.argwhere(probs==np.max(probs)))]
    # 取最大值对应的下标值
    action_probs = zip(board.available, probs)
    return action_probs, 0


class TreeNode(object):
    """A node in the MCTS tree. Each node keeps track of its own value Q,
    prior probability P, and its visit-count-adjusted prior score u.
    """

    def __init__(self, parent, prior_p):
        self._parent = parent
        self._children = {}  # dict action:TreeNode
        self._n_visits = 0
        self._Q = 0
        self._u = 0
        self._P = prior_p

    def update(self, leaf_value):
        # Count visit.
        self._n_visits += 1
        # Update Q, a running average of values for all visits.
        self._Q = self._Q + 1.0 * (leaf_value - self._Q) / self._n_visits

    def get_value(self, c_puct):
        self._u = self._P * c_puct * \
            np.sqrt(np.log(self._parent._n_visits) / (0.1 + self._n_visits))
        return self._Q + self._u

    def is_leaf(self):
        return self._children == {}

    def is_root(self):
        return self._parent is None


class MCTS(object):
    """A simple implementation of Monte Carlo Tree Search."""

    def __init__(self, policy_value_fn, c_puct=5, simulate_time=10):
        """
        policy_value_fn:策略函数
        c_puct :控制深度优先，还是广度优先。参见UCB公式
        simulate_time:每次模拟时间，单位是秒
        """
        self._root = TreeNode(None, 1.0)
        self._root._n_visits = 0
        self._policy = policy_value_fn
        self._c_puct = c_puct
        self.simulate_time = datetime.timedelta(seconds=simulate_time)

    def _selection(self, board):
        node = self._root
        while not node.is_leaf():
            # Greedily select next move.
            action, node = max(node._children.items(),
                               key=lambda act_node: act_node[1].
                               get_value(self._c_puct))
            board.set_action(action)
            board.next_states()
        return board, node

    def _expansion(self, board, node):
        action_probs, _ = self._policy(board)
        # extand all children node
        for action, probs in action_probs:
            if action not in node._children:
                node._children[action] = TreeNode(node, probs)

    def _simulation(self, board):
        # Evaluate the leaf node by random rollout
        player = board.moved_player
        end, winner = board.game_end()
        while len(board.available) > 0 and not end:
            action_probs = rollout_policy_fn(board)
            max_action = max(action_probs, key=itemgetter(1))[0]
            board.set_action(max_action)
            end, winner = board.game_end()
            if end:
                break
            board.next_states()

        if winner == -1:  # tie
            leaf_value = 0
        else:
            leaf_value = 1 if winner == player else -1

        return leaf_value

    def _backpropagation(self, node, leaf_value):
        # Update value and visit count of nodes in this traversal.
        node.update(leaf_value)
        while node._parent:
            node = node._parent
            leaf_value = -leaf_value
            node.update(leaf_value)

    def _playout(self, board):
        # Selection
        board, node = self._selection(board)
        # Expansion
        self._expansion(board, node)
        # Simulation
        leaf_value = self._simulation(board)
        # Backpropagation
        self._backpropagation(node, leaf_value)

    def get_move(self, board):

        begin = datetime.datetime.utcnow()
        while datetime.datetime.utcnow() - begin < self.simulate_time:
            board_copy = copy.deepcopy(board)
            self._playout(board_copy)

        # 选择访问次数最多的节点，不是最高胜率的节点，访问次数多结果更可信
        return max(self._root._children.items(),
                   key=lambda act_node: act_node[1]._n_visits)[0]

    def update_with_move(self, move):
        self._root = TreeNode(None, 1.0)

    def __str__(self):
        return "MCTS"
