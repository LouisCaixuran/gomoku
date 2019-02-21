# encoding: utf-8
class Gomoku(object):
    def __init__(self):
        self.width=9
        self.height=9
        self.status=['-' for i in range(self.height*self.width)]
        self.available=[i for i in range(self.height*self.width)]
        self.last_action=-1
        self.players=['X','O']
        self.width=9
        self.height=9


    def play(self,player1,player2):
        self.player1=player1
        self.player2=player2
        self.current_player=player1
        self.showboard()
        while True:
            self.last_action=self.current_player.get_action()
            self.set_chessman(self.last_action)
            self.showboard()
            end,winner=self.game_end()
            if end:
                break
        if winner!=-1:
            print(self.status[self.last_action]," wins")
        else:
            print("it is tied")


    def game_end(self):
        if self.is_won()==True :
            if self.current_player==self.player1:
                return True,self.player2
            else:
                return True,self.player1
        elif len(self.available)==0:
            return True,-1
        else:
            return False,-1


    def showboard(self):
        print('   '),
        for i in range(self.width):
            print("  {pi}".format(pi=i)),
        print
        for i in range(self.width):
            print
            print("  {pi}".format(pi=i)),
            for j in range(self.height):
                print("  {pi}".format(pi=self.status[self.width*i+j])),
            print
        print("last action is",self.last_action%self.width,self.last_action//self.height)

    def set_chessman(self,action):
    	player=self.current_player
    	self.last_action=action
        if player==self.player1:
            self.status[action]='X'
        else:
            self.status[action]='O'
        self.available.remove(action)
        if player==self.player1:
            self.current_player=self.player2
        else:
            self.current_player=self.player1

    def is_won(self):
    	if self.last_action==-1:
    		return False
        player=self.status[self.last_action]
        pos=self.last_action
        c=0
        for i in range(pos-pos%9,pos-pos%9+9):
            if self.status[i]==player:
                c+=1
            else:
                c=0
            if c>=5:
                return True
        c=0
        for i in range(pos%9,pos%9+73,9):
            if self.status[i]==player:
                c+=1
            else:
                c=0
            if c>=5:
                return True
        c=0
        for i in range(pos%10,80,10):
            if self.status[i]==player:
                c+=1
            else:
                c=0
            if c>=5:
                return True
            if i%9==8:
                c=0

        c=0
        for i in range(pos%8,80,8):
            if self.status[i]==player:
                c+=1
            else:
                c=0
            if c>=5:
                return True
            if i%9==0:
                c=0
        return False

