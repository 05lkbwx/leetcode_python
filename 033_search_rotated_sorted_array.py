# world's fastest
def search(nums, target):
    if not nums:
        return -1
    lo, hi = 0, len(nums) - 1
    infinity = 2**31
    while lo < hi:
        mid = (lo + hi) / 2
        # if nums[mid] and target are "on the same side"
        number = 0
        if (nums[0] > nums[mid]) == (nums[0] > target):
            number = nums[mid]
        elif nums[0] > target:
            # not the same side
            number = -infinity
        else:
            number = infinity

        if number < target:
            lo = mid + 1
        else:
            hi = mid
    return lo if nums[lo] == target else -1

# # my solution
# def search(nums, target):
# 	if not nums:
# 		return -1

# 	l, r = 0, len(nums) - 1
# 	print nums
# 	while l < r:
# 		m = int((l + r) / 2)
# 		if nums[m] > nums[r]:
# 			l = m + 1
# 		else:
# 			r = m

# 	setoff = 0
# 	target_array = nums[:r]
# 	if target <= nums[len(nums) - 1]:
# 		setoff = r
# 		target_array = nums[r:]

# 	if not target_array:
# 		return -1

# 	l, r = 0, len(target_array) - 1
# 	while l <= r:
# 		m = (l + r) / 2
# 		if target_array[m] < target:
# 			l = m + 1
# 		elif target_array[m] > target:
# 			r = m - 1
# 		else:
# 			return setoff + m

# 	return -1

if __name__ == '__main__':
	nums = [1, 3]
	target = 1
	print search(nums, target)
	# print 'hw'