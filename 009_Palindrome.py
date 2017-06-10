# world's fastest
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    # multiplier = cmp(x, 0)
    s = str(x)
    return s == s[::-1]

# my solution
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    x = '#'.join(x)
    for i in range(int((2 * len(x) - 1) / 2) + 1):
    	if x[i] != x[len(x) - 1 - i]:
    		return False
    return True
    
if __name__ == '__main__':
	x = 232132
	print isPalindrome(x)