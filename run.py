from board import Gomoku
from player import Humanplayer

def run():
    chess=Gomoku()
    chess.init_board()
    chess.showboard()
    player1=Humanplayer('x')
    player2=Humanplayer('y')
    c=0
    while True:
        if c%2==0:
            n=raw_input("please p1 enter position:")
            player1.humaninput(n)
            chess.set_chessman(player1)
            chess.showboard()
            if chess.is_wonman(player1):
        	   print "player1 win"
        	   break
    
        else:
            n=raw_input("please p2 enter position:")
            player2.humaninput(n)
            chess.set_chessman(player2)
            chess.showboard()
            if chess.is_wonman(player2):
        	   print "player2 win"
        	   break
        c=c+1
        if c==225:
            print "it is tied"
            break

if __name__ == '__main__':
    run()
