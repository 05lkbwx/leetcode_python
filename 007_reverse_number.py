## world's fastest
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x >= 0 else -1
    s = str(abs(x))
    rs = s[::-1]
    ri = sign * int(rs)
    
    result = ri
    if sign > 0:
        if ri > 2 ** 31 - 1:
            result = 0
    elif ri < -2 ** 31:
        result = 0
    
    return result

## my solution:
# def reverse(x):
#     """
#     :type x: int
#     :rtype: int
#     """	
#     multiplier = 1
#     if x < 0:
#     	x = -1 * x
#     	multiplier = -1

#     result = 0
#     while x > 0:
#     	result = 10 * result + x % 10
#     	x = x / 10

#     if result > 2147483647:
#     	return 0

#     return multiplier * result
        
if __name__ == '__main__':
	x = 123
	print reverse(x)

	x = -123
	print reverse(x)

# 2,147,483,647