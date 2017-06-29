# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# world's fastest
def swapPairs(self,head):
    if not head or not head.next:return head

    dummy=ListNode(-1)
    dummy.next=head
    p=dummy
    while p.next and p.next.next:
        #反向.
        tmp=p.next.next
        p.next.next=tmp.next
        tmp.next=p.next
        p.next=tmp
        
        p=p.next.next

    return dummy.next

# # my solution
# def swapPairs(head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
#     if not head:
#     	return []

#     head_ptr = ListNode(0)
#     head_ptr.next = head
#     cur_ptr  = head_ptr

#     while cur_ptr.next:
#         if cur_ptr.next.next:
#     	    A = cur_ptr.next
#     	    B = cur_ptr.next.next
#     	    cur_ptr.next = B
#     	    next_ptr     = B.next
#     	    B.next       = A
#     	    A.next       = next_ptr
#     	    cur_ptr      = A
#         else:
#             return head_ptr.next
            
#     return head_ptr.next

if __name__ == '__main__':
