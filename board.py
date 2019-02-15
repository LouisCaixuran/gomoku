# encoding: utf-8
class Gomoku(object):
    def __init__(self):
        self.board = [[0 for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                self.board[i][j] = '-'

    def play(self,player1,player2):
    	self.player1=player1
    	self.player2=player2

    def showboard(self):
    	print(' '),
        for i in range(9): 
            print i,
        print
        for i in range(9):
            print i,
            for j in range(9):
                print self.board[i][j],
            print

    def set_chess(self,pos,color):
        self.board[pos[0]][pos[1]] = color        

    def get_chess(self,pos):
        return self.board[pos[0]][pos[1]]

    def set_chessman(self,player):
        pos = player.get_pos()
        if player==self.player1:
        	color='X'
        else:
        	color='O'
        self.set_chess(pos,color)

    def is_won(self,player):
    	pos=player.get_pos()
    	if player==self.player1:
        	color='X'
        else:
        	color='O'
        start_x = 0
        end_x = 8
        if pos[0] -4 >=0:
            start_x =pos[0] - 4
        if pos[0] +4 <=8:
            end_x = pos[0]+4
        count = 0
        for pos_x in range(start_x, end_x+1):
            if self.get_chess((pos_x, pos[1])) == color:
                count +=1
                if count >=5:
                    return True
            else:
                count = 0
       
        start_y = 0
        end_y = 8
        if pos[1] -4 >=0:
            start_y =pos[1] - 4
        if pos[1] +4 <=8:
            end_y = pos[1]+4

        count = 0
        
        for pos_y in range(start_y, end_y+1):
            if self.get_chess((pos[0], pos_y)) == color:
                count +=1
                if count >=5:
                    return True
            else:
                count = 0

        count = 0
        s=pos[0] - pos[1]
        start=start_x
        end=end_y+s
        if pos[0]>pos[1]:
            start=start_y+s
            end=end_x
        for index in range(start, end+1):
            if self.get_chess((index, index-s)) == color:
                count +=1
                if count >=5:
                    return True
            else:
                count = 0

        count = 0
        s=pos[0] + pos[1]
        if pos[0]+pos[1]<=5:
            start=start_x
            end=s-start_y

        if pos[0]+pos[1]>3:
            start=s-start_y
            end=start_x

        if s>=0 and s<=9:
            for index in range(start, end+1):
                if self.get_chess((index, s-index)) == color:
                    count +=1
                    if count >=5:
                        return True
                else:
                    count = 0
        return False