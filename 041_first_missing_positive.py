# world's fastest 32 ms:
def firstMissingPositive(nums):
    l = len(nums)
    if(l==0):
        return 1
    temp = [0]*(l+1)
    for x in nums:
        if(x >0 and x <= l ):
            temp[x] = 1
    for i in range(1,l+1):
        if(temp[i] == 0):
            return i
    return l+1

# 2nd fastest 33 ms:
def firstMissingPositive(nums):
    l = len(nums)
    dic = {}
    for i in range(l):
        dic[nums[i]]=True
    for i in range(1,l+1):
        if not dic.get(i):
            return i
    return l+1

# # my solution
# def firstMissingPositive(nums):
# 	nums = sorted(nums)
# 	res  = 0
# 	for i, v in enumerate(nums):
# 		if v <= res:
# 			continue
# 		if v == res + 1:
# 			res += 1
# 		else:
# 			return res + 1
# 	return res + 1

if __name__ == '__main__':
	print firstMissingPositive([3,4,-1,1])