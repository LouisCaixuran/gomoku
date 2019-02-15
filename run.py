from board import Gomoku
from player import HumanPlayer

def run():
    chess=Gomoku()
    player1=HumanPlayer(chess)
    player2=HumanPlayer(chess)
    chess.play(player1,player2)
    chess.showboard()
    c=0
    while True:
        if c%2==0:
            player1.get_action()
            chess.set_chessman(player1)
            chess.showboard()
            if chess.is_won(player1):
        	   print "player1 win"
        	   break
    
        else:
            player2.get_action()
            chess.set_chessman(player2)
            chess.showboard()
            if chess.is_won(player2):
        	   print "player2 win"
        	   break
        c=c+1
        if c==225:
            print "it is tied"
            break

if __name__ == '__main__':
    run()
