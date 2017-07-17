def solveSudoku(self, board):
    self.board = board
    self.solve()

def findUnassigned(self):
    for row in range(9):
        for col in range(9):
            if self.board[row][col] == ".":
                return row, col
    return -1, -1

def solve(self):
    row, col = self.findUnassigned()
    #no unassigned position is found, puzzle solved
    if row == -1 and col == -1:
        return True
    for num in ["1","2","3","4","5","6","7","8","9"]:
        if self.isSafe(row, col, num):
            self.board[row][col] = num
            if self.solve():
                return True
            self.board[row][col] = "."
    return False
        
def isSafe(self, row, col, ch):
    boxrow = row - row%3
    boxcol = col - col%3
    if self.checkrow(row,ch) and self.checkcol(col,ch) and self.checksquare(boxrow, boxcol, ch):
        return True
    return False

def checkrow(self, row, ch):
    for col in range(9):
        if self.board[row][col] == ch:
            return False
    return True

def checkcol(self, col, ch):
    for row in range(9):
        if self.board[row][col] == ch:
            return False
    return True
   
def checksquare(self, row, col, ch):
    for r in range(row, row+3):
        for c in range(col, col+3):
            if self.board[r][c] == ch:
                return False
    return True

# import numpy as np
# def solveSudokuHelper(board, row_remain, col_remain, ept_remain):
# 	pos = ept_remain[0]
# 	new_brd = board.copy()
# 	new_row = row_remain[:]
# 	new_col = col_remain[:]
# 	# new_blk = blk_remain[:]
# 	new_ept = ept_remain[1:]

# 	small_board = board[3 * pos[0] : 3 * (pos[0] + 1), 3 * pos[1] : 3 * (pos[1] + 1)]
# 	remains = set(['1','2','3','4','5','6','7','8','9']) - set([s for s in [y for x in small_board for y in x] if s != '.'])

# 	cad = row_remain[pos[0]] & col_remain[pos[1]] & remains

# 	if not cad:
# 		return False

# 	if not new_ept:
# 		return True

# 	for s in cad:
# 		new_brd[pos[0], pos[1]] = s
# 		new_row[pos[0]] = row_remain[pos[0]] - set([s])
# 		new_col[pos[1]] = col_remain[pos[1]] - set([s])
# 		# new_blk[pos[0] / 3][pos[1] / 3] = blk_remain[pos[0] / 3][pos[1] / 3] - set([s])

# 		# print 'pos is,', [pos[0], pos[1]]
# 		# print 'board is,'
# 		# print new_brd
# 		# print 'new row is,', new_row
# 		# print 'new col is,', new_col
# 		# # print 'new blk is,', new_blk
# 		# print 'empty remain is,', new_ept

# 		if solveSudokuHelper(new_brd, new_row, new_col, new_ept):
# 			return True

# 	return False

# def solveSudoku(board):
#     """
#     :type board: List[List[str]]
#     :rtype: void Do not return anything, modify board in-place instead.
#     """
#     row_remain = [set([]) for _ in range(9)]
#     col_remain = [set([]) for _ in range(9)]
#     blk_remain = [[set([]) for _ in range(3)] for _ in range(3)]
#     ept_remain = []
#     nums       = ['1','2','3','4','5','6','7','8','9']

#     board = np.array(board)
#     for i in range(9):
#     	row_remain[i] = set(nums) - set(board[i, :])

#     for i in range(9):
#     	col_remain[i] = set(nums) - set(board[:, i])

#     for i in range(9):
#     	for j in range(9):
#     		if board[i, j] == '.':
#     			ept_remain.append([i, j])

#     return solveSudokuHelper(board, row_remain, col_remain, ept_remain)

if __name__ == '__main__':
	board = [
	['5', '3', '.', '.', '7', '.', '.', '.', '.'],
	['6', '.', '.', '1', '9', '5', '.', '.', '.'],
	['.', '9', '8', '.', '.', '.', '.', '6', '.'],
	['8', '.', '.', '.', '6', '.', '.', '.', '3'],
	['4', '.', '.', '8', '.', '3', '.', '.', '1'],
	['7', '.', '.', '.', '2', '.', '.', '.', '6'],
	['.', '6', '.', '.', '.', '.', '2', '8', '.'],
	['.', '.', '.', '4', '1', '9', '.', '.', '5'],
	['.', '.', '.', '.', '8', '.', '.', '7', '9']
	]
	print solveSudoku(board)
	# print 'hw'

