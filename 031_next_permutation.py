# world's fastest
def nextPermutation(nums):
    if not nums:
        return None

    j = k = 0
    # Find the first index(j) break the trend: nums[i-1] >= nums[i]
    for i in range(len(nums)-1, -1, -1):
        if nums[i-1] < nums[i]:
            j = i-1
            k = i
            break

    # Find the smallest number which is larger than nums[j], the break point
    for i in range(len(nums)-1, j, -1):
        if nums[i] > nums[j]:
            nums[j], nums[i] = nums[i], nums[j]    # swap position
            break

    nums[k:] = sorted(nums[k:])        # sort rest
    return

# # my solution:
# def nextPermutation(nums):
# 	if len(nums) < 2:
# 		return

# 	max_val = nums[len(nums) - 1]
# 	for i in range(1, len(nums), 1):
# 		if nums[len(nums) - 1 - i] >= max_val:
# 			max_val = nums[len(nums) - 1 - i]
# 		else:
# 			for j in range(0, i, 1):
# 				if nums[len(nums) - 1 - j] > nums[len(nums) - 1 - i]:
# 					temp = nums[len(nums) - 1 - j]
# 					nums[len(nums) - 1 - j] = nums[len(nums) - 1 - i]
# 					nums[len(nums) - 1 - i] = temp
# 					nums[len(nums) - i : ] = nums[len(nums) - i : ][::-1]
# 					return

# 	nums = nums.reverse()
# 	return

if __name__ == '__main__':
	# nums = [1,1,5]
	nums = [3,2,1]
	# nums = [1,2,3]
	# nums = [1]
	nextPermutation(nums)
	print nums