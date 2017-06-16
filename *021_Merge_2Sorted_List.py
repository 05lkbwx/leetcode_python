# world's fastest
def mergeTwoLists(l1, l2):    
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    
    dummy1 = TreeNode(-1)
    dummy1.next= l1
    current = dummy1
    
    while l1 and l2:
        if l1.val<l2.val:
            l1=l1.next
        else:
            next = current.next
            current.next = l2
            tmp = l2.next
            l2.next = next
            l2 = tmp
        current= current.next
    current.next = l1 or l2
    return dummy1.next


# # my solution
# def mergeTwoLists(l1, l2):
#     pre_pt = []
#     cur_pt = []
#     l      = []
#     while l1 and l2:
# 		if l1.val < l2.val:
# 			cur_pt = l1
# 			l1 = l1.next
# 		else:
# 			cur_pt = l2
# 			l2 = l2.next

# 		if not l:
# 			l = cur_pt
# 		if pre_pt:
# 			pre_pt.next = cur_pt
# 		pre_pt = cur_pt

#     if l2:
#     	cur_pt = l2
#     	if not l:
# 			l = cur_pt
#     	if pre_pt:
#     		pre_pt.next = cur_pt
# 		pre_pt = cur_pt
#     elif l1:
#     	cur_pt = l1
#     	if not l:
# 			l = cur_pt
#     	if pre_pt:
#     		pre_pt.next = cur_pt
# 		pre_pt = cur_pt
#     else:
#         pass
    
#     return l
        
if __name__ == '__main__':
	print 'hw'
