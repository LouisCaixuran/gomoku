from board import Gomoku
from player import *


def run():
    chess=Gomoku()
    player1=RandomPlayer(chess)
    player2=MCTSPlayer(chess)
    chess.play(player1,player2)

    

if __name__ == '__main__':
    run()
