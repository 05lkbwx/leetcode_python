# world's fastest
def myAtoi(self, str):
    """
    :type str: str
    :rtype: int
    """
    ls = list(str.strip());
    if len(ls) == 0 : return 0
    b = 1
    if ls[0] == '-':
        b = -1
    if ls[0] in ['-', '+'] :
        del ls[0]
    ret, i = 0, 0
    while i < len(ls) and ls[i].isdigit():
        # print (ord(ls[i]))
        ret = 10*ret + ord(ls[i])-ord('0')
        i += 1
    return max(-2**31, min(b*ret, 2**31-1))

# # my solution
# def myAtoi(str):
#     """
#     :type str: str
#     :rtype: int
#     """
#     str = str.lstrip()
#     if str == "":
#     	return 0

#     str = str.split()[0]
#     sign = 1
#     if str[0] == "-":
#     	sign = -1
#     	str  = str[1:]
#     elif str[0] == "+":
#     	str  = str[1:]
#     else:
#     	pass

#     if str == "":
#     	return 0

#     number = 0
#     i = 0
#     while i < len(str) and str[i].isdigit():
#     	i = i + 1

#     if i == 0:
#     	return 0

#     number = sign * int(str[0:i])
#     if number > 2147483647:
#     	return 2147483647
#     if number < -2147483648:
#     	return -2147483648

#     return number 

if __name__ == '__main__':
	str = "   -0012a421 "
	print myAtoi(str)