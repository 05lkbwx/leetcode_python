# world's fastest
def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    count = {}
    for x in nums:
        count[x] = count.get(x, 0) + 1
    uniqueNums = count.keys()
    pos = [x for x in uniqueNums if x >= 0]
    neg = [x for x in uniqueNums if x < 0]
    pos.sort()
    neg.sort(reverse=True)

    res = []
    if 0 in count and count[0] > 2:
        res.append([0, 0, 0])
    for p in pos:
        for n in neg:
            r = 0-p-n
            if (r == p or r == n) and count[r] > 1:
                res.append([p,n,r])
            elif r in count and (r > p or r < n):
                res.append([p,n,r]) 
    return res

# # my solution
# import itertools
# def twoSumTable(neg):
#     neg_2sum = {}
#     for i in range(0, len(neg), 1):
#     	for j in range(i + 1, len(neg), 1):
#     		ni = neg[i]
#     		nj = neg[j]
#     		if not abs(ni + nj) in neg_2sum:
#     			neg_2sum[abs(ni + nj)] = [[ni, nj]]
#     		else:
#     			neg_2sum[abs(ni + nj)].append([ni, nj])

#     for key, value in neg_2sum.iteritems():
#     	value.sort()
#     	neg_2sum[key] = [k for k,_ in itertools.groupby(value)]
    	
#     return neg_2sum

# def combine_2Sum_1Sum(sum2, sum1):
# 	keys = list(set(sum1.keys()).intersection(set(sum2.keys())))
# 	result = []
# 	for x in keys:
# 		for y in sum2[x]:
# 	 		result.append(sorted(y + [sum1[x]]))
# 	return result

# def threeSum(nums):
#     neg = sorted([x for x in nums if x < 0])
#     pos = sorted([x for x in nums if x >= 0])
#     pos_2sum = twoSumTable(pos)
#     neg_2sum = twoSumTable(neg)
#     pos_1sum = {x : x for x in pos}
#     neg_1sum = {-1 * x : x for x in neg}

#     print combine_2Sum_1Sum(neg_2sum, pos_1sum)
#     print combine_2Sum_1Sum(pos_2sum, neg_1sum)
#     return combine_2Sum_1Sum(neg_2sum, pos_1sum) + combine_2Sum_1Sum(pos_2sum, neg_1sum)
   
if __name__ == '__main__':
	nums = [-1, 0, 1, 2, -1, -4]
	print threeSum(nums)
