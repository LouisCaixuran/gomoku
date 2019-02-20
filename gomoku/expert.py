# encoding: utf-8
level = 9
grade = 10
MAX = 1008611
def scan(chesspad, color):

	shape = [[[0 for high in range(5)] for col in range(9)] for row in range(9)]
 # 扫描每一个点，然后在空白的点每一个方向上做出价值评估！！
	for i in range(9):
		for j in range(9):

# 如果此处为空 那么就可以开始扫描周边
			if chesspad[i][j] ==0:
				m = i
				n = j
  # 如果上方跟当前传入的颜色参数一致，那么加分到0位！
				while n - 1 >= 0 and chesspad[m][n - 1] == color:
					n -= 1
					shape[i][j][0] += grade
				if n-1>=0 and chesspad[m][n - 1] == 0:
					shape[i][j][0] += 1
				if n-1 >= 0 and chesspad[m][n - 1] == -color:
					shape[i][j][0] -= 2
				m = i
				n = j
# 如果下方跟当前传入的颜色参数一致，那么加分到0位！
				while (n + 1 < level and chesspad[m][n + 1] == color):
					n += 1
					shape[i][j][0] += grade
				if n + 1 < level and chesspad[m][n + 1] == 0:
					shape[i][j][0] += 1
				if n + 1 < level and chesspad[m][n + 1] == -color:
					shape[i][j][0] -= 2
				m = i
				n = j
  # 如果左边跟当前传入的颜色参数一致，那么加分到1位！
				while (m - 1 >= 0 and chesspad[m - 1][n] == color):
					m -= 1
					shape[i][j][1] += grade
				if m - 1 >= 0 and chesspad[m - 1][n] == 0:
					shape[i][j][1] += 1
				if m - 1 >= 0 and chesspad[m - 1][n] == -color:
					shape[i][j][1] -= 2
				m = i
				n = j
  # 如果右边跟当前传入的颜色参数一致，那么加分到1位！
				while (m + 1 < level and chesspad[m + 1][n] == color):
					m += 1
					shape[i][j][1] += grade
				if m + 1 < level and chesspad[m + 1][n] == 0:
					shape[i][j][1] += 1
				if m + 1 < level and chesspad[m + 1][n] == -color:
					shape[i][j][1] -= 2
				m = i
				n = j
  # 如果左下方跟当前传入的颜色参数一致，那么加分到2位！
				while (m - 1 >= 0 and n + 1 < level and chesspad[m - 1][n + 1] == color):
					m -= 1
					n += 1
					shape[i][j][2] += grade
				if m - 1 >= 0 and n + 1 < level and chesspad[m - 1][n + 1] == 0:
					shape[i][j][2] += 1
				if m - 1 >= 0 and n + 1 < level and chesspad[m - 1][n + 1] == -color:
					shape[i][j][2] -= 2
				m = i
				n = j
  # 如果右上方跟当前传入的颜色参数一致，那么加分到2位！
				while (m + 1 < level and n - 1 >= 0 and chesspad[m + 1][n - 1] == color):
					m += 1
					n -= 1
					shape[i][j][2] += grade
				if m + 1 < level and n - 1 >= 0 and chesspad[m + 1][n - 1] == 0:
					shape[i][j][2] += 1
				if m + 1 < level and n - 1 >= 0 and chesspad[m + 1][n - 1] == -color:
					shape[i][j][2] -= 2
				m = i
				n = j
  # 如果左上方跟当前传入的颜色参数一致，那么加分到3位！
				while (m - 1 >= 0 and n - 1 >= 0 and chesspad[m - 1][n - 1] == color):
					m -= 1
					n -= 1
					shape[i][j][3] += grade
				if m - 1 >= 0 and n - 1 >= 0 and chesspad[m - 1][n - 1] == 0:
					shape[i][j][3] += 1
				if m - 1 >= 0 and n - 1 >= 0 and chesspad[m - 1][n - 1] == -color:
					shape[i][j][3] -= 2
					m = i
					n = j
  # 如果右下方跟当前传入的颜色参数一致，那么加分到3位！
				while m + 1 < level and n + 1 < level and chesspad[m + 1][n + 1] == color:
					m += 1
					n += 1
					shape[i][j][3] += grade
				if m + 1 < level and n + 1 < level and chesspad[m + 1][n + 1] == 0:
					shape[i][j][3] += 1
				if m + 1 < level and n + 1 < level and chesspad[m + 1][n + 1] == -color:
					shape[i][j][3] -= 2
	return shape
 
 
def sort(shape):
	for i in shape:
		for j in i:
			for x in range(5):
				for w in range(3, x - 1, -1):
					if j[w - 1] < j[w]:
						temp = j[w]
						j[w - 1] = j[w]
						j[w] = temp
	return shape
 
 
def evaluate(shape):
	for i in range(level):
		for j in range(level):
 
			if shape[i][j][0] == 4:
				return i, j, MAX
			shape[i][j][4] = shape[i][j][0]*1000 + shape[i][j][1]*100 + shape[i][j][2]*10 + shape[i][j][3]
			max_x = 0
			max_y = 0
			max = 0
	for i in range(9):
		for j in range(9):
			if max < shape[i][j][4]:
				max = shape[i][j][4]
				max_x = i
				max_y = j

	return max_x, max_y,max
 
 
def get_max_value_pos(board):
	chesspad=[[0 for j in range(9)]for i in range(9)]
	for i in range(9):
		for j in range(9):
			if board[i*9+j]=='X':
				chesspad[i][j]=1
			elif board[i*9+j]=='O':
				chesspad[i][j]=-1

	shape_P = scan(chesspad, 1)
	shape_C=scan(chesspad,-1)
	shape_P = sort(shape_P)
	shape_C = sort(shape_C)
	max_x_P, max_y_P, max_P = evaluate(shape_P)
	max_x_C, max_y_C, max_C = evaluate(shape_C)
	if max_P>max_C and max_C<MAX:
		return max_x_P,max_y_P
	else:
		return max_x_C,max_y_C


 
 
