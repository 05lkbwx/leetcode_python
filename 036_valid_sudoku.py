# world's fastest:
def isValidSudoku(board):
    sudokurow = [{} for _ in range(9)]
    sudokucol = [{} for _ in range(9)]
    sudokublock = [[{} for _ in range(3)] for _ in range(3)]
    
    for i in range(9):
        for j in range(9):
            element = board[i][j]
            if element == '.':
                continue

            if element in sudokurow[i]:
                return False
            else:
                sudokurow[i][element] = 1

            if element in sudokucol[j]:
                return False
            else:
                sudokucol[j][element] = 1

            if element in sudokublock[i//3][j//3]:
                return False
            else:
                sudokublock[i//3][j//3][element] = 1

    return True

# # my solution:
# import itertools 
# import numpy as np
# def isValidSudoku(board):
# 	# 1. all elements are in ['1', '2', '3', '4', '5', '6', '7', '8', '9']??
# 	board_elems = list(itertools.chain.from_iterable(board))
# 	board_elems = set([s for s in board_elems if s != '.'])
# 	if board_elems - set(['1', '2', '3', '4', '5', '6', '7', '8', '9']) != set([]):
# 		return False

# 	# 2. rows
# 	for row in board:
# 		temp = [s for s in row if s != '.']
# 		if len(temp) != len(list(set(temp))) or set(temp) - set(['1', '2', '3', '4', '5', '6', '7', '8', '9']) != set([]):
# 			return False

# 	# 3. columns
# 	board = zip(*board)
# 	for row in board:
# 		temp = [s for s in row if s != '.']
# 		if len(temp) != len(list(set(temp))) or set(temp) - set(['1', '2', '3', '4', '5', '6', '7', '8', '9']) != set([]):
# 			return False

# 	# 4. 9 cubic
# 	board = zip(*board)
# 	board = np.array(board)
# 	for i in range(3):
# 		for j in range(3):
# 			small_board = board[3 * i : 3 * (i + 1), 3 * j : 3 * (j + 1)]
# 			temp = [s for s in [y for x in small_board for y in x] if s != '.']
# 			if len(temp) != len(list(set(temp))) or set(temp) - set(['1', '2', '3', '4', '5', '6', '7', '8', '9']) != set([]):
# 				return False

# 	return True


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

	print isValidSudoku(board)

