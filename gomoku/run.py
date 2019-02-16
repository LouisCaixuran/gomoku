from board import Gomoku
from player import HumanPlayer

def run():
    chess=Gomoku()
    player1=HumanPlayer(chess)
    player2=HumanPlayer(chess)
    chess.play(player1,player2)

    

if __name__ == '__main__':
    run()
