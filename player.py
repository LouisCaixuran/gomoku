# encoding: utf-8
class Gomoku(object):
    def __init__(self):
        self.board = [[0 for i in range(16)] for j in range(16)]

    def init_board(self):
        for i in range(1,16):
            for j in range(1,16):
                self.board[i][j] = '+'

    def showboard(self):
        print '  ',
        for i in range(1,16):
            c = chr(ord('a') + i-1) 
            print c,
        print
        for i in range(1,16):
            if i<=9 and i >=1:
                print '',
            print i,
            for j in range(1,16):
                print self.board[i][j],
            print

    def set_chess(self,pos,color):
        self.board[pos[0]][pos[1]] = color        

    def get_chess(self,pos):
        return self.board[pos[0]][pos[1]]

    def set_chessman(self,player):
        pos = player.get_pos()
        color = player.get_color()
        self.set_chess(pos,color)

    def is_won(self,pos,color):
        start_x = 1
        end_x = 15
        if pos[0] -4 >=1:
            start_x =pos[0] - 4
        if pos[0] +4 <=15:
            end_x = pos[0]+4
        count = 0
        for pos_x in range(start_x, end_x+1):
            if self.get_chess((pos_x, pos[1])) == color:
                count +=1
                if count >=5:
                    return True
            else:
                count = 0
       
        start_y = 1
        end_y = 15
        if pos[1] -4 >=1:
            start_y =pos[1] - 4
        if pos[1] +4 <=15:
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
        if pos[0]+pos[1]<=16:
            start=start_x
            end=s-start_y

        if pos[0]+pos[1]>16:
            start=s-start_y
            end=start_x

        if s>=6 and s<=12:
            for index in range(start, end+1):
                if self.get_chess((index, s-index)) == color:
                    count +=1
                    if count >=5:
                        return True
                else:
                    count = 0
        return False

    def is_wonman(self,player):
        pos = player.get_pos()
        color = player.get_color()
        return self.is_won(pos,color)


class Player(object):
    def __init__(self,color):
        pass

    def get_pos(self):
        pass

    def get_color(self):
        pass

    
class Humanplayer(Player):
    def __init__(self,color):
        self.color=color

    def set_pos(self,pos):
        self.pos = pos

    def get_pos(self):
        return self.pos

    def get_color(self):
        return self.color
    
    def humaninput(self,s):
        ret = s.split(',')
        pos_x = int(ret[0])
        pos_y = ord(ret[1]) - ord('a') +1
        self.set_pos((pos_x, pos_y))





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


