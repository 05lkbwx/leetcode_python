import numpy as np

## fastest:
def maxArea(height):
	left,right  = 0,len(height) - 1
	res,tempRes = 0,0
	while left < right:
		if height[left] < height[right]:
			tempRes = (right - left) * height[left]
			if  tempRes > res:
				res = tempRes
			left += 1
		else:
			tempRes = (right - left) *height[right]
			if tempRes > res:
				res = tempRes
			right -= 1
	return res

# # my solution
# def maxArea(height):
# 	j = len(height) - 1
# 	i = 0
# 	mx = 0

# 	while i < j:
# 		mx = max(mx, (j - i) * min(height[i], height[j]))
# 		if height[i] < height[j]:
# 			i = i + 1
# 		elif height[i] >= height[j]:
# 			j = j - 1
# 	return mx

if __name__ == '__main__':
	height = [3,2,2,3]
	print maxArea(height)