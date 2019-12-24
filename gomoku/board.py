# encoding: utf-8
import numpy as np


class Gomoku(object):
    def __init__(self,board_size=15,n_long=5):
        self.size=board_size
        self.width=self.size
        self.height=self.size
        self.n_long=n_long
        self.status=[0 for i in range(self.height*self.width)]
        self.available=[i for i in range(self.height*self.width)]
        self.player1=1
        self.player2=2
        self.player1_last_action=-1
        self.player2_last_action=-1
        
        self.last_action=-1
        self.end=False
        self.winner=-1
        self.current_player=1
        self.moved_player=0 

    def play(self,player1,player2,isShow=False):
        if isShow:
            self.showboard()
        while True:
            if self.end:
                break
            
            self.last_action=self.get_current_player(player1,player2).get_action()
            self.set_action(self.last_action)
            if isShow :
                self.showboard()
                
            self.end,self.winner=self.game_end()


            self.next_states() # change current player
            #update web ui
            self.get_current_player(player1,player2).reply(self.last_action//self.size,
                                    self.last_action%self.size)

        if self.end:#update web ui
            player1.reply(self.last_action//self.size,
                                    self.last_action%self.size)
            player2.reply(self.last_action//self.size,
                                    self.last_action%self.size)
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
            if self.moved_player==self.player1:
                return True,1
            else:
                return True,2
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

        print("The Current player:",self.current_player)
        if self.last_action != -1 :
            print("player1: O, last action:" ,self.player1_last_action//self.height,self.player1_last_action%self.width)
            print("player2: X, last action:" ,self.player2_last_action//self.height,self.player2_last_action%self.width)

    def set_action(self,action):
        self.moved_player=self.current_player
        self.last_action=action

        if self.moved_player==self.player1:
            self.status[action]=1
            self.player1_last_action=action
        else:
            self.status[action]=2
            self.player2_last_action=action
        self.available.remove(action)
   
    def next_states(self):
        if self.moved_player==self.player1:                #next player become current player
            self.current_player=self.player2
        else:
            self.current_player=self.player1

    def is_won(self):
        n = self.n_long
        player_moved=[] 

        if self.last_action==-1:
            return False

        for m in range(self.width*self.height):
            if self.status[m] == self.moved_player:
                player_moved.append(m)

        if len(player_moved) < n: # player move less 5
            return False
        
        for m in player_moved:
            h = m // self.width
            w = m % self.width
    
            if (w in range(self.width - n + 1) and
                len(set(self.status[i] for i in range(m, m + n))) == 1):
                return True

            if (h in range(self.height - n + 1) and
                len(set(self.status[i] for i in range(m, m + n * self.width, self.width))) == 1):
                return True

            if (w in range(self.width - n + 1) and h in range(self.height - n + 1) and
                len(set(self.status[i] for i in range(m, m + n * (self.width + 1), self.width + 1))) == 1):
                return True

            if (w in range(n - 1, self.width) and h in range(self.height - n + 1) and
                len(set(self.status[i] for i in range(m, m + n * (self.width - 1), self.width - 1))) == 1):
                return True
        return False

    def current_state(self):
        state=np.zeros((4,self.height,self.width))
        for i in range(self.height*self.width):
            if self.status[i]==1:
                state[0,i//self.width,i%self.width]=1
                
            if self.status[i]==2:
                state[1,i//self.width,i%self.width]=1
            
        if self.current_player==2:
            state[3]=0
        else:
            state[3]=1
        state[2,self.last_action//self.width,self.last_action%self.width]=1
        return state
        
    
