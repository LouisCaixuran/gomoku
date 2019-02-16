# encoding: utf-8
class Gomoku(object):
    def __init__(self):
        self.status=['-' for i in range(81)]
        self.avaliable=[i for i in range(81)]

    def change(self,x,y):
    	return 9*x+y

  

    def play(self,player1,player2):
    	self.player1=player1
    	self.player2=player2
    	self.current_player=player1
    	self.showboard()
    	while True:
            self.current_player.get_action()
            self.set_chessman(self.current_player)
            self.showboard()
            if self.is_won():
        	   	print self.status[self.change(self.last_action[0],self.last_action[1])]," win"
        	   	break
			if len(self.avaliable)==0:
				print "It is tied"
				break

    def showboard(self):
    	print(' '),
        for i in range(9): 
            print i,
        print
        for i in range(9):
            print i,
            for j in range(9):
                print self.status[9*i+j],
            print

    def set_chessman(self,player):
        pos = player.get_pos()
        if player==self.player1:
        	self.status[9*pos[0]+pos[1]]='X'
        else:
        	self.status[9*pos[0]+pos[1]]='O'
        self.avaliable.remove(9*pos[0]+pos[1])
        self.last_action=pos
        if player==self.player1:
        	self.current_player=self.player2
        else:
        	self.current_player=self.player1

    def is_won(self):
    	n=self.change(self.last_action[0],self.last_action[1])
    	player=self.status[n]
    	pos=self.last_action
        c=0
        for i in range(pos[0]*9,pos[0]*9+8):
        	if self.status[i]==player:
        	    c+=1
        	else:
        		c=0
        	if c>=5:
        		return True
        c=0
        for i in range(pos[1],pos[1]+72,9):
        	if self.status[i]==player:
				c+=1
        	else:
        		c=0
        	if c>=5:
        		return True
        c=0
        for i in range(n%10,80,10):
        	if self.status[i]==player:
				c+=1
        	else:
        		c=0
        	if c>=5:
        		return True
        	if i%9==8:
        		c=0

        c=0
        for i in range(n%8,80,8):
        	if self.status[i]==player:
				c+=1
        	else:
        		c=0
        	if c>=5:
        		return True
        	if i%9==0:
        		c=0
        return False

