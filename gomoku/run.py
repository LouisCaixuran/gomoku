from board import Gomoku
from player import HumanPlayer, MCTSPlayer, RandomPlayer, ExpertPlayer
import logging
import argparse


def log_config():
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    logging.basicConfig(filename='gomoku.log',
                        level=logging.DEBUG,
                        format=LOG_FORMAT,
                        datefmt=DATE_FORMAT)


def run():
    parse = argparse.ArgumentParser(description="gomoku program")
    parse.add_argument("player1", type=int, choices=[1, 2, 3, 4],
                       help="1.Human; 2.MCTS; 3.Random; 4.Expert")

    parse.add_argument("player2", type=int, choices=[1, 2, 3, 4],
                       help="1.Human; 2.MCTS; 3.Random; 4.Expert")

    parse.add_argument("--size", type=int, default=8,
                       help="The Board size,default is 8*8 ")

    parse.add_argument("--simulate_time", type=int, default=2,
                       help="The MCTS playout simulation time,default is 2s ")

    args = parse.parse_args()
    chess = Gomoku(board_size=args.size)
    p1 = {
        1: HumanPlayer(chess),
        2: MCTSPlayer(chess, simulate_time=args.simulate_time),
        3: RandomPlayer(chess),
        4: ExpertPlayer(chess)}

    p2 = {
        1: HumanPlayer(chess),
        2: MCTSPlayer(chess, simulate_time=args.simulate_time),
        3: RandomPlayer(chess),
        4: ExpertPlayer(chess)}

    chess.play(p1[args.player1], p2[args.player2], isShow=True)


if __name__ == '__main__':
    log_config()
    run()
