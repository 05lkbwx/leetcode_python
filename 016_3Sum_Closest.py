# world's fastest:
def threeSumClosest(self, nums, target):
    nums.sort()
    if target <= 0:
        out = abs(sum(nums[:3])-target)
        out_sum = sum(nums[:3])
        n=len(nums)
        for i in xrange(n):
            j,k=i+1,n-1
            while j<k:
                isum=nums[i]+nums[j]+nums[k]
                if abs(isum-target) < out:
                    out = abs(isum-target)
                    out_sum = isum
                if isum > target:
                    k-=1
                elif isum < target:
                    j+=1
                elif isum==target:
                    return isum
            if nums[i]>0:
                return out_sum
        return out_sum
    if target > 0:
        nums = nums[::-1]
        out = abs(sum(nums[:3])-target)
        out_sum = sum(nums[:3])
        n=len(nums)
        for i in xrange(n):
            j,k=i+1,n-1
            while j<k:
                isum=nums[i]+nums[j]+nums[k]
                if abs(isum-target) < out:
                    out = abs(isum-target)
                    out_sum = isum
                if isum < target:
                    k-=1
                elif isum > target:
                    j+=1
                elif isum==target:
                    return isum
            if nums[i]<0:
                return out_sum
        return out_sum


# # my solution:
# def threeSumClosest(nums, target):
# 	nums = sorted(nums)
# 	best_diff = abs(nums[0] + nums[1] + nums[2] - target)
# 	best_comb = [nums[0], nums[1], nums[2]]
# 	for i in range(len(nums) - 2):
# 		j, k, t = i + 1, len(nums) - 1, target - nums[i]
# 		while j < k:
# 			cur = nums[j] + nums[k]
# 			if abs(cur - t) < best_diff:
# 				best_diff = abs(cur - t)
# 				best_comb = [nums[i], nums[j], nums[k]]
# 			if cur > t:
# 				k = k - 1
# 			elif cur < t:
# 				j = j + 1
# 			else:
# 				return sum(best_comb)
# 	return sum(best_comb)

if __name__ == '__main__':
	nums = [-1, 2, 1, -4]
	target = 1
	print threeSumClosest(nums, target)