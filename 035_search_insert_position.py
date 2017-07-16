# world's fastest
def searchInsert(self, nums, target):
    l = 0
    h = len(nums)
    while l < h:
        mid = (l+h) >> 1
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            h = mid
    return h

# my solution
def searchInsert(nums, target):
    if not nums:
    	return 0
    l, r = 0, len(nums) - 1
    while l <= r:
    	m = (l + r) / 2
    	if nums[m] > target:
    		r = m - 1
    	elif nums[m] < target:
    		l = m + 1
    	else:
    		return m
    return (r + 1)

if __name__ == '__main__':
	print searchInsert([1,3,5,6], 0)