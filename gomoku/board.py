# encoding: utf-8
class Gomoku(object):
    def __init__(self):
        self.ar=15
        self.width=self.ar
        self.height=self.ar
        self.status=[0 for i in range(self.height*self.width)]
        self.available=[i for i in range(self.height*self.width)]
        self.last_action=-1
        self.players=[1,2]
        self.end=False
        self.winner=-1
        self.current_player=1

    def play(self,player1,player2,isShow=False):
        self.player1=1
        self.player2=2
        if isShow:
            self.showboard()
        while True:
            self.last_action=self.get_current_player(player1,player2).get_action()

            self.set_chessman(self.last_action)
            if isShow :
                self.showboard()
            self.end,self.winner=self.game_end()
            if not self.end:
                self.get_current_player(player1,player2).reply(self.last_action//self.ar,
                                    self.last_action%self.ar)
            else:
                player1.reply(self.last_action//self.ar,
                                    self.last_action%self.ar)
                player2.reply(self.last_action//self.ar,
                                    self.last_action%self.ar)
                break
        if self.winner!=-1:
            print(self.status[self.last_action]," wins")
        else:
            print("it is tied")

    def get_current_player(self,player1,player2):
        if self.current_player==1:
            return player1
        else:
            return player2


    def game_end(self):
        if self.is_won()==True :
            if self.current_player==self.player1:
                return True,2
            else:
                return True,1
        elif len(self.available)==0:
            return True,-1
        else:
            return False,-1


    def showboard(self):
        import os
        os.system('clear')
        print("    ",end="")
        for i in range(self.width):
            print("{pi: ^4}".format(pi=i),end=""),
        print(" ")
        for i in range(self.width):
            print(" ")
            print("{pi: ^4}".format(pi=i),end=""),
            for j in range(self.height):
                if self.status[self.width*i+j]==1:
                    p = 'O'
                elif self.status[self.width*i+j]==2:
                    p = 'X'
                else:
                    p = '-'
                print("{pi: ^4}".format(pi=p),end=""),
            print("")
        if self.last_action != -1 :
            print("last action is",self.last_action//self.height,self.last_action%self.width)

    def set_chessman(self,action):
        player=self.current_player
        self.last_action=action

        if player==self.player1:
            self.status[action]=1
        else:
            self.status[action]=2
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
        for i in range(pos-pos%self.ar,pos-pos%self.ar+self.ar):
            if self.status[i]==player:
                c+=1
            else:
                c=0
            if c>=5:
                return True
        c=0
        for i in range(pos%self.ar,pos%self.ar+self.ar*(self.ar-1),self.ar):
            if self.status[i]==player:
                c+=1
            else:
                c=0
            if c>=5:
                return True
        c=0
        for i in range(pos%(self.ar+1),self.ar**2-1,self.ar+1):
            if self.status[i]==player:
                c+=1
            else:
                c=0
            if c>=5:
                return True
            if i%self.ar==self.ar-1:
                c=0

        c=0
        for i in range(pos%(self.ar-1),self.ar**2-1,self.ar-1):
            if self.status[i]==player:
                c+=1
            else:
                c=0
            if c>=5:
                return True
            if i%self.ar==0:
                c=0
        return False

