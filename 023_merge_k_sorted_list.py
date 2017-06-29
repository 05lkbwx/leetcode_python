# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# world's fastest
def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    wl = []
    for l in lists:
        while l:
            wl.append(l.val)
            l = l.next
    wl.sort()    
    start = r = ListNode(0)
    for val in wl:
        r.next = ListNode(val)
        r = r.next
    return start.next

## my solution
# def mergeKLists(lists):
#     """
#     :type lists: List[ListNode]
#     :rtype: ListNode
#     """
#     if lists:
#     	for i, l in enumerate(lists):
#     		if not l:
#     			del lists[i]

#     print lists

#     if not lists:
#     	return []

#     head_ptr = ListNode(None)
#     cur_ptr  = head_ptr

#     while lists:
#     	obj_i, obj_val = 0, lists[0].val
#     	for i, l in enumerate(lists):
#     		if l.val < obj_val:
#     			obj_i, obj_val = i, l.val

#     	cur_ptr.next = lists[obj_i]
#     	cur_ptr      = cur_ptr.next
#     	lists[obj_i] = lists[obj_i].next
#     	if not lists[obj_i]:
#     		del lists[obj_i]

# 	return head_ptr.next

if __name__ == '__main__':
	lists = []
	lists = [l for l in lists if l]
	print lists 