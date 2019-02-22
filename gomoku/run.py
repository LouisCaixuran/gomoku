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

    if args.player1==1:
        player1=HumanPlayer(chess)
    elif args.player1==2:
        player1=MCTSPlayer(chess)
    elif args.player1==3:
        player1=RandomPlayer(chess)
    else:
        player1=ExpertPlayer(chess)

    if args.player2==1:
        player2=HumanPlayer(chess)
    elif args.player2==2:
        player2=MCTSPlayer(chess)
    elif args.player2==3:
        player2=RandomPlayer(chess)
    else:
        player2=ExpertPlayer(chess)
    
    chess.play(player1,player2)

    

if __name__ == '__main__':
    log_config()
    run()
