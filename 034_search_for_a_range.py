# world's fastest
def searchRange(nums, target):
    if len(nums) == 0:
        return [-1,-1]
    s, e = 0, len(nums) - 1
    res0 = -1
    while s < e:
        mid = (s+e)/2
        val = nums[mid]
        if val > target:
            e = mid - 1
        elif val == target:
            e = mid
        elif val < target:
            s = mid + 1
    res0 = s if nums[s] == target else -1
    s, e = 0, len(nums) - 1
    res1 = -1
    while s < e:
        mid = (s+e)/2
        val = nums[mid]
        if val > target:
            e = mid - 1
        elif val == target:
            if nums[mid+1] == target:
                s = mid + 1
            else:
                s = mid 
                break
        elif val < target:
            s = mid + 1
    res1 = s if nums[s] == target else -1
    return [res0,res1]

# # my solution:
# def searchRange(nums, target):
#     if not nums:
#     	return [-1, -1]

#     res = [-1, -1]
# 	l, r = 0, len(nums) - 1
# 	while l <= r:
# 		m = (l + r) / 2
# 		print 'l, r, m is,', l, r, m 
# 		if nums[m] < target:
# 			l = m + 1
# 		elif (nums[m] == target) and ((m == 0) or (m > 0 and nums[m - 1] < target)):
# 			res[0] = m
# 			break
# 		elif (nums[m] > target) and ((m == 0) or (m > 0 and nums[m - 1] < target)):
# 			return [-1, -1]
# 		else:
# 			r = m - 1

#     l, r = 0, len(nums) - 1
#     while l <= r:
# 		m = (l + r) / 2
# 		print 'l, r, m is,', l, r, m 
# 		if nums[m] > target:
# 			r = m - 1
# 		elif (nums[m] == target) and ((m == len(nums) - 1) or (m < len(nums) - 1 and nums[m + 1] > target)):
# 			res[1] = m
# 			break
# 		elif (nums[m] < target) and ((m == len(nums) - 1) or (m < len(nums) - 1 and nums[m + 1] > target)):
# 			return [-1, -1]
# 		else:
# 			l = m + 1

#     return res

if __name__ == '__main__':
	print searchRange([5, 7, 7, 8, 8, 10], 8)
	# print 'hw'