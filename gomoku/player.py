class Player(object):
    def __init__(self):
        pass

    def get_action(self):
        pass
    
class HumanPlayer(Player):
    def __init__(self,board):
    	self.board=board

    def set_pos(self,pos):
        self.pos = pos

    def get_pos(self):
        return self.pos

    
    def get_action(self):
    	while True:
    		n=raw_input("please enter position:")
        	ret = n.split(',')
        	x=int(ret[0])
        	y=int(ret[1])
        	if x>=0 and x<9 and y>=0 and y<9:
        		if self.board.board[x][y]=='-':
        			break
        	print("invalid input")
        self.set_pos((x, y))







