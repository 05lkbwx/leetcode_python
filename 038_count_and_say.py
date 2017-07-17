# world's fastest
def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    s = "1"
    if n == 1: return s
    
    for i in range(n-1):
        a = s[0]
        tmp = ""
        count = 1
        for i in range(1,len(s)):
            if s[i] == a:
                count += 1
            else:
                tmp += str(count)+a
                a = s[i]
                count = 1
        tmp += str(count) + a
        s = tmp
        
    return s

# # my solution
# def countAndSay(n):
# 	if n == 1:
# 		return '1'

# 	res   = '1'
# 	for _ in range(n - 1):
# 		print res
# 		count = 0
# 		s     = res[0]
# 		new_res = ''
# 		for i, v in enumerate(res):
# 			if v == s:
# 				count += 1
# 			else:
# 				new_res += str(count)
# 				new_res += s
# 				s = v
# 				count = 1
# 			if  i == len(res) - 1:
# 				new_res += str(count)
# 				new_res += s
# 		res = new_res

# 	return res

if __name__ == '__main__':
	print countAndSay(6)