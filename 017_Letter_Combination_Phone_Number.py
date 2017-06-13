# worlds's fastest
def letterCombinations(digits):
    if digits == "":
        return []
    c = [""]
    dic = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz" }
    
    for digit in digits:
        nc = []
        for letter in dic[digit]:
            for prev_letters in c:
                nc.append ( prev_letters + letter )
        c = nc
    return c

# # my solution
# import itertools
# def letterCombinations(digits):
# 	digits = list(digits)
# 	if len(digits) == 0: return []
# 	if '1' in digits: return []

# 	num_letter_table = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z'], '0':[' ']}
# 	cur_result = num_letter_table[digits[0]]
# 	for i in digits[1:]:
# 		prev_result = cur_result
# 		cur_result  = list(itertools.chain.from_iterable([[(x + j) for x in prev_result] for j in num_letter_table[i]]))
# 	return cur_result

if __name__ == '__main__':
	digits = ''
	print letterCombinations(digits)