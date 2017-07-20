# world's fastest
def trap(height):
    if len(height) == 0:
        return 0
    l, r = 0, len(height) - 1
    leftheight, rightheight = height[l], height[r]
    ret = 0
    while l < r:
        if height[l] < height[r]:
            if leftheight > height[l]:
                ret += leftheight - height[l]
            else:
                leftheight = height[l]
            l += 1
        else:
            if rightheight > height[r]:
                ret += rightheight - height[r]
            else:
                rightheight = height[r]
            r -= 1
    return ret

# # my solution
# def trap(height):
# 	if not height:
# 		return 0
# 	vol = 0
# 	l, r = 0, len(height) - 1
# 	while l < r:
# 		if height[l] <= height[r]:
# 			l1 = l + 1
# 			while height[l] >= height[l1]:
# 				if l1 == r:
# 					return vol
# 				vol += height[l] - height[l1] 
# 				l1  += 1
# 			l = l1
# 		else:
# 			r1 = r - 1
# 			while height[r] >= height[r1]:
# 				if r1 == l:
# 					return vol
# 				vol += height[r] - height[r1]
# 				r1  -= 1
# 			r = r1
# 	return vol

if __name__ == '__main__':
	print trap([0,1,0,2,1,0,1,3,2,1,2,1])
