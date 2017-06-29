# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# world's fastest
def reverseKGroup(head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head
    while True:
        count = 0
        while r and count < k:
            count += 1
            r = r.next
        if count == k:
            pre, cur = r,l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur
            jump.next, jump, l = pre, l, r
        else:
            return dummy.next

# # my solution
# def reverseKGroup(head, k):
#     """
#     :type head: ListNode
#     :type k: int
#     :rtype: ListNode
#     """
# 	vals = []
# 	p    = head
# 	while p:
# 		vals.append(p.val)
# 		p = p.next

# 	if len(vals) < k:
# 		return head

# 	for i in range(len(vals) / k):
# 		vals[i * k : (i + 1) * k] = reversed(vals[i * k : (i + 1) * k])

# 	null_head = ListNode(0)
# 	p         = null_head
# 	for v in vals:
# 		p.next = ListNode(v)
# 		p      = p.next

# 	return null_head.next

if __name__ == '__main__':
	a = [0,1,2,3,4]
	print a[0:2]
	print a[2:4]
