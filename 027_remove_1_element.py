# world's fastest
def removeElement(nums, val):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        if nums[0] == val:
            return 0
        else:
            return 1
    st = ll = 0
    end = len(nums) - 1
    swap = 0
    while end > st:
        while nums[st] != val and end > st:
            st += 1
            if st == end:
                ll = st
        while nums[end] == val and end > st:
            end -= 1
            if st == end:
                ll = st + 1

        if end > st:
            tmp = nums[st]
            nums[st] = nums[end]
            nums[end] = tmp
            st += 1
            if st == end:
                ll = st
            end -= 1

    if nums[st] == val:
        return st
    else:
        return st + 1


# # my solution
# def removeElement(nums, val):
#     """
#     :type nums: List[int]
#     :type val: int
#     :rtype: int
#     """
#     if not nums:
#     	return 0

#     dst_pos = 0
#     for v in nums:
#     	if v != val:
#     		nums[dst_pos] = v
#     		dst_pos += 1

#     return dst_pos

if __name__ == '__main__':
	print 'hw'
	