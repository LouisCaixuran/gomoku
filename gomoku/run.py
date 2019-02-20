from board import Gomoku
from player import *

def run():
    print "player:1.HumanPlayer; 2.MCTSPlayer; 3.RandomPlayer; 4.ExpertPlayer"
    chess=Gomoku()
    player1=input("please choose player1:")
    if player1==1:
        player1=HumanPlayer(chess)
    elif player1==2:
        player1=MCTSPlayer(chess)
    elif player1==3:
        player1=RandomPlayer(chess)
    else:
        player1=ESTPlayer(chess)

    player2=input("please choose player2:")
    if player2==1:
        player2=HumanPlayer(chess)
    elif player2==2:
        player2=MCTSPlayer(chess)
    elif player2==3:
        player2=RandomPlayer(chess)
    else:
        player2=ESTPlayer(chess)
    
    chess.play(player1,player2)

    

if __name__ == '__main__':
    run()
