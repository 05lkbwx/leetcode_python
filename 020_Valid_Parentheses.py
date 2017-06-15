# world's fastest:
def isValid(s):
    pars = [('(', ')'), ('[', ']'), ('{', '}')]
    opener = dict(pars)
    closer = dict(map(lambda i: (i[1], i[0]), pars))
    
    stack = []
    
    for c in s:
        if c in opener:
            stack.append(opener.get(c))
        else:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                return False
            
    if stack:
        return False
    else: 
        return True


# # my solution
# def isValid(s):
# 	if len(s) == 0:
# 		return True
# 	parentheses_dict = {'(':[], '{':[], '[':[]}
# 	for i, v in enumerate(s):
# 		if v == '(':
# 			parentheses_dict['('].append(i)
# 		elif v == '{':
# 			parentheses_dict['{'].append(i)
# 		elif v == '[':
# 			parentheses_dict['['].append(i)
# 		else:
# 			if len(parentheses_dict['(']) == 0 and len(parentheses_dict['{']) == 0 and len(parentheses_dict['[']) == 0:
# 				return False
# 			else:
# 				yuan_left_last_pos = -1
# 				if len(parentheses_dict['(']) != 0:
# 					yuan_left_last_pos = parentheses_dict['('][-1]

# 				hua_left_last_pos  = -1
# 				if len(parentheses_dict['{']) != 0:
# 					hua_left_last_pos  = parentheses_dict['{'][-1]

# 				fang_left_last_pos = -1
# 				if len(parentheses_dict['[']) != 0:
# 					fang_left_last_pos = parentheses_dict['['][-1]

# 				if v == ')':
# 					if yuan_left_last_pos == max(yuan_left_last_pos, hua_left_last_pos, fang_left_last_pos):
# 						del parentheses_dict['('][-1]
# 					else:
# 						return False
# 				elif v == '}':
# 					if hua_left_last_pos == max(yuan_left_last_pos, hua_left_last_pos, fang_left_last_pos):
# 						del parentheses_dict['{'][-1]
# 					else:
# 						return False
# 				else:
# 					if fang_left_last_pos == max(yuan_left_last_pos, hua_left_last_pos, fang_left_last_pos):
# 						del parentheses_dict['['][-1]
# 					else:
# 						return False

# 	if len(parentheses_dict['(']) == 0 and len(parentheses_dict['{']) == 0 and len(parentheses_dict['[']) == 0:
# 		return True
# 	return False

if __name__ == '__main__':
	s = '([)]'
	print isValid(s)