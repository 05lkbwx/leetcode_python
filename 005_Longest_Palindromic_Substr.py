# manacher's algorithm
def longestPalindrome(s):
    # Transform S into T.
    # For example, S = "abba", T = "^#a#b#b#a#$".
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0
    for i in range (1, n-1):
        P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
        # Attempt to expand palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum element in P.
    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]

## my solution
# def longestPalindrome(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     record = ''
#     for i in range(2 * len(s) + 1):
#     	cur_array = ''
#     	left_pos  = i - 1
#     	right_pos = i + 1

#     	if i % 2 == 1:
#     		cur_array = s[(i - 1) / 2]
#     		left_pos  = i - 2
#     		right_pos = i + 2

#     	while left_pos >= 0 and right_pos <= 2 * len(s) and s[(left_pos - 1) / 2] == s[(right_pos - 1) / 2]:
#     		cur_array = s[(left_pos - 1) / 2] + cur_array + s[(right_pos - 1) / 2]
#     		left_pos  = left_pos  - 2
#     		right_pos = right_pos + 2

#     	if len(cur_array) > len(record):
#     		record = cur_array
#     # print 'longest length of palindromic substring is,', len(record)
#     return record
   
if __name__ == '__main__':
	s = 'cbbd'
	print longestPalindrome(s)