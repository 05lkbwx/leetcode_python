# world's fastest
def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    x = []
    if n < 4:
        return []
    for i in xrange(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue
        for j in xrange(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                continue
            k = j + 1
            l = n - 1
            r = nums[i] + nums[j]
            while k < l:
                s = r + nums[k] + nums[l]
                if s < target:
                    k += 1
                elif s > target:
                    l -= 1
                else:
                    x.append([nums[i], nums[j], nums[k], nums[l]])
                    while k < l and nums[k] == nums[k + 1]:
                        k += 1
                    while k < l and nums[l] == nums[l - 1]:
                        l -= 1
                    k += 1
                    l -= 1
    return x

# # a very good general solution
# def fourSum(self, nums, target):
#     def findNsum(nums, target, N, result, results):
#         if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
#             return
#         if N == 2: # two pointers solve sorted 2-sum problem
#             l,r = 0,len(nums)-1
#             while l < r:
#                 s = nums[l] + nums[r]
#                 if s == target:
#                     results.append(result + [nums[l], nums[r]])
#                     l += 1
#                     while l < r and nums[l] == nums[l-1]:
#                         l += 1
#                 elif s < target:
#                     l += 1
#                 else:
#                     r -= 1
#         else: # recursively reduce N
#             for i in range(len(nums)-N+1):
#                 if i == 0 or (i > 0 and nums[i-1] != nums[i]):
#                     findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

#     results = []
#     findNsum(sorted(nums), target, 4, [], results)
#     return results

if __name__ == '__main__':
	nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
	target = 5
	print fourSum(nums, target)