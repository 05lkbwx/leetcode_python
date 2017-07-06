# world's fastest
def longestValidParentheses(s):
    lenS = len(s)
    if lenS <= 1:
		return 0
    scan = []
    maxNum = 0
    flag = -1
    for i in xrange(lenS):
		if s[i] == '(':
			if flag != -1:
				scan.append(flag)
				flag = -1
			else:
				scan.append(i)
		else:
			if scan:
				index = scan.pop()
				maxNum = max(maxNum, i-index+1)
				flag = index
			else:
				flag = -1
    return maxNum

# my solution
def longestValidParentheses(s):
    cur_stack = []
    max_len   = -1
    for i, v in enumerate(s):
    	if v == "(":
    		cur_stack.append(i)
    	else:
    		if not cur_stack:
    			cur_stack.append(i)
    		else:
    			if s[cur_stack[-1]] == ")":
    				cur_stack.append(i)
    			else:
    				cur_stack.pop()
    cur_stack = [-1] + cur_stack + [len(s)]
    cur_stack = [cur_stack[i] - cur_stack[i - 1] - 1 for i in range(1, len(cur_stack), 1)]
    return max(cur_stack)

if __name__ == '__main__':
	# s = ')()())'
	s = '(()'
	print longestValidParentheses(s)