import numpy as np

## fastest c++ translate to python:
def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    M = len(s)
    N = len(p)
    dp = np.zeros((M + 1, N + 1), dtype = bool)
    dp[M][N] = True

    j = N - 1
    while j >= 0:
    	if p[j] == '*':
    		j = j - 1
    		dp[M][j] = dp[M][j + 2]
    	j = j - 1

    i = M - 1
    while i >= 0:
    	j = N - 1
    	while j >= 0:
    		if p[j] == '*':
    			j = j - 1
    			dp[i][j] = (p[j] == '.' or p[j] == s[i]) and (dp[i + 1][j + 2] or dp[i + 1][j])
    			dp[i][j] = dp[i][j] or dp[i][j + 2]
    		elif p[j] == '.' or p[j] == s[i]:
    			dp[i][j] = dp[i + 1][j + 1]
    		else:
    			pass
    		j = j - 1
    	i = i - 1

    return dp[0][0]

## my solution:
# def isMatch_helper(i, j, s1, s2, M):
# 	n1 = len(s1) / 2
# 	n2 = len(s2) / 2
# 	if M[i][j] != -1:
# 		return M[i][j]

# 	result = 0
# 	if i == n1 and j == n2:
# 		M[i][j] = 1
# 		return 1
# 	elif i == n1:
# 		if s2[2 * j + 1] == '*':
# 			result = isMatch_helper(i, j + 1, s1, s2, M)
# 		else:
# 			result = 0
# 		M[i][j + 1] = result
# 		return result
# 	elif j == n2:
# 		if s1[2 * i + 1] == '*':
# 			result = isMatch_helper(i + 1, j, s1, s2, M)
# 		else:
# 			result = 0
# 		M[i + 1][j] = result
# 		return result
# 	else:
# 		if s1[2 * i + 1] == '*' or s2[2 * j + 1] == '*':
# 			if s1[2 * i + 1] == '*' and s2[2 * j + 1] != '*' and s1[2 * i] != '.' and s2[2 * j] != '.' and s1[2 * i] != s2[2 * j]:
# 				result = isMatch_helper(i + 1, j, s1, s2, M)
# 			elif s1[2 * i + 1] != '*' and s2[2 * j + 1] == '*' and s1[2 * i] != '.' and s2[2 * j] != '.' and s1[2 * i] != s2[2 * j]:
# 				result = isMatch_helper(i, j + 1, s1, s2, M)
# 			else:
# 				result = isMatch_helper(i + 1, j, s1, s2, M) or isMatch_helper(i, j + 1, s1, s2, M) or isMatch_helper(i + 1, j + 1, s1, s2, M)
# 		elif s1[2 * i] == '.' or s2[2 * j] == '.':
# 			result = isMatch_helper(i + 1, j + 1, s1, s2, M)
# 		elif s1[2 * i] == s2[2 * j]:
# 			result = isMatch_helper(i + 1, j + 1, s1, s2, M)
# 		else:
# 			result = 0

# 		M[i][j] = result
# 		return result

# def reconstruct_string(s):
# 	result = ''
# 	for i in range(len(s)):
# 		result = result + s[i]
# 		if i < len(s) - 1 and s[i] != '*' and s[i + 1] != '*':
# 			result = result + '#'
# 		elif i == len(s) - 1 and s[i] != '*':
# 			result = result + '#'
# 	return result 

# def isMatch(s, p):
#     """
#     :type s: str
#     :type p: str
#     :rtype: bool
#     """
#     s = reconstruct_string(s)
#     p = reconstruct_string(p)
#     print s 
#     print p
#     M  = -1 * np.ones((len(s) / 2 + 1, len(p) / 2 + 1))
#     result = isMatch_helper(0, 0, s, p, M)
#     if result == 0.0:
#     	return False
#     return True

if __name__ == '__main__':
	print isMatch("aa","a")
	print isMatch("aa","aa")
	print isMatch("aaa","aa")
	print isMatch("aa", "a*")
	print isMatch("aa", ".*")
	print isMatch("ab", ".*")
	print isMatch("aab", "c*a*b")
	print isMatch("bbbba", ".*a*a")
	print isMatch('a', 'ab*')
