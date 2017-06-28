# world's fastest
def generateParenthesis(n):
    def recur_build(curr_str, l_unmatch_count, l_total):
        if len(curr_str) == 2*n:
            return [curr_str, ]
        output = []
        if l_total < n:
            output = recur_build(curr_str + '(', l_unmatch_count + 1, l_total + 1)
        if l_unmatch_count > 0:
            output += recur_build(curr_str + ')', l_unmatch_count - 1, l_total)
        return output
    return recur_build('', 0, 0)

# # my solution
# def generateParenthesis(n):
# 	def generateParenthesis_helper(n, M):
# 		if M[n] == []:
# 			if n == 0:
# 				M[n] = ["()"]
# 			else:
# 				A = generateParenthesis_helper(n - 1, M)
# 				for v in A:
# 					M[n].append("(" + v + ")")
# 				for i in range(n):
# 					A = generateParenthesis_helper(i, M)
# 					B = generateParenthesis_helper(n - 1 - i, M)
# 					for u in A:
# 						for v in B:
# 							M[n].append(u + v)
# 		return M[n]

# 	M = {key:[] for key in range(n)}
# 	generateParenthesis_helper(n - 1, M)
# 	return list(set(M[n - 1]))

if __name__ == '__main__':
	n = 3
	print generateParenthesis(n)
