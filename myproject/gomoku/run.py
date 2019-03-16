from board import Gomoku
from player import *
import logging
import argparse

def log_config():
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    logging.basicConfig(filename = 'gomoku.log', 
                        level=logging.DEBUG,
                        format=LOG_FORMAT,
                        datefmt=DATE_FORMAT)

def run():
    parse=argparse.ArgumentParser(description="gomoku program")
    parse.add_argument("player1", type=int, choices=[1,2,3,4],
                    help="1.HumanPlayer; 2.MCTSPlayer; 3.RandomPlayer; 4.ExpertPlayer")

    parse.add_argument("player2", type=int, choices=[1,2,3,4],
                    help="1.HumanPlayer; 2.MCTSPlayer; 3.RandomPlayer; 4.ExpertPlayer")

    args = parse.parse_args()
    chess=Gomoku()
    p1={
        1 : HumanPlayer(chess),
        2 : MCTSPlayer(chess),
        3 : RandomPlayer(chess),
        4 : ExpertPlayer(chess)}

    p2={
        1 : HumanPlayer(chess),
        2 : MCTSPlayer(chess),
        3 : RandomPlayer(chess),
        4 : ExpertPlayer(chess)}

    chess.play(p1[args.player1],p2[args.player2])

    

if __name__ == '__main__':
    log_config()
    run()
