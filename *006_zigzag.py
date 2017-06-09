# world's fastest
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows < 2 or len(s) < numRows: return s
    rows = [""] * numRows
    ind, step = 0, 1
    for v in s:
        rows[ind] += v
        if ind == 0:
            step = 1
        elif ind == numRows - 1:
            step = -1
        ind += step
    return ''.join(rows)

# my solution
# def convert(s, numRows):
#     """
#     :type s: str
#     :type numRows: int
#     :rtype: str
#     """
#     if numRows == 1:
#     	return s

#     result = ''
#     for i in range(numRows):
#     	if i == 0:
#     		k = 0
#     		while k * 2 * (numRows - 1) < len(s):
#     			result = result + s[k * 2 * (numRows - 1)]
#     			k = k + 1
#     	elif i == (numRows - 1):
#     		k = 0
#     		while (k * 2 + 1) * (numRows - 1) < len(s):
#     			result = result + s[(k * 2 + 1) * (numRows - 1)]
#     			k = k + 1
#     	else:
# 	    	k = 0
# 	    	stop_flag = False
# 	    	while stop_flag == False:
# 	    		if (k * 2 * (numRows - 1) + i) < len(s):
# 	    			result = result + s[k * 2 * (numRows - 1) + i]
# 	    		else:
# 	    			stop_flag = True
# 	    		if ((k + 1) * 2 * (numRows - 1) - i) < len(s):
# 	    			result = result + s[(k + 1) * 2 * (numRows - 1) - i]
# 	    		else:
# 	    			stop_flag = True
# 	    		k = k + 1
#     return result

if __name__ == "__main__":
	# s = 'A'
	# numRows = 1
	# print convert(s, numRows)

	numRows = 3
	rows = [""] * numRows
	print type(rows)
	print rows
