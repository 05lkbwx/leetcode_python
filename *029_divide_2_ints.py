import sys

# world's fastest
def divide(dividend, divisor):
    dd, dr = dividend, divisor
    positive = (dd>0) is (dr>0)
    dd, dr = abs(dd), abs(dr)
    ans = 0
    while dd >= dr:
        num, i = dr, 1
        while dd >= num:
            dd -= num
            ans += i
            num <<= 1
            i <<= 1
    if not positive:
        ans =- ans
    return max(-2**31, min(ans, 2**31-1))

# # 1 solution
# def divide(dividend, divisor):
#     positive = (dividend < 0) is (divisor < 0)
#     dividend, divisor = abs(dividend), abs(divisor)
#     res = 0
#     while dividend >= divisor:
#         temp, i = divisor, 1
#         while dividend >= temp:
#             dividend -= temp
#             res += i
#             i <<= 1
#             temp <<= 1
#     if not positive:
#         res = -res
#     return min(max(-2147483648, res), 2147483647)

## my solution
# def divide(dividend, divisor):
#     """
#     :type dividend: int
#     :type divisor: int
#     :rtype: int
#     """
#     if divisor == 0:
#     	return sys.maxint

#     twos    = []
#     multips = []
#     i, j = 1, abs(divisor)
#     while i < sys.maxint:
#     	twos.append(i)
#     	multips.append(j)
#     	i += i
#     	j += j

#     res  = abs(dividend)
#     frac = 0
#     while res >= abs(divisor):
#     	for i in range(len(twos)):
#     		if multips[i] > res:
#     			res  -= multips[i - 1]
#     			frac += twos[i - 1]
#     			break

#     if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
#     	if res != 0:
#     		return -frac - 1
#     	else:
#     	    return -frac
    	    
#     return frac

if __name__ == '__main__':
	print divide(-2147483648, -1)
