# world's fastest
def removeDuplicates(self, nums):
    if not nums:
        return 0
    
    prev, length = nums[0], 1
    for num in nums[1:]:
        if num != prev:
            nums[length] = num
            length += 1
            prev = num
    return length

# # my solution
# def removeDuplicates(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if not nums:
#     	return 0

#     count = 1
#     prev_uniq_num = nums[0]

#     for v in nums:
#     	if v != prev_uniq_num:
#     		nums[count] = v
#     		prev_uniq_num = v
#     		count += 1 

#     nums = nums[0:count]
#     return count

if __name__ == '__main__':
	nums = [1,1,2]
	print removeDuplicates(nums)