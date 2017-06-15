class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# world's fastest
def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    buf = {}
    count = 0
    cur = head
    while cur:
        buf[count] = cur
        cur = cur.next
        count += 1
    if count == 1 or count == 0:
        return None
    if n == count:
        return buf[1]
    buf[count - n - 1].next = buf[count - n- 1].next.next
    return head

## my solution:
# def removeNthFromEnd(head, n):
#     """
#     :type head: ListNode
#     :type n: int
#     :rtype: ListNode
#     """
#     vals = [head.val]
#     while head.next != None:
#     	head = head.next
#     	vals.append(head.val)

#     if n > len(vals):
#     	return []
#     del vals[-n]

#     if len(vals) == 0:
#     	return []

#     head = ListNode(vals[-1])
#     del vals[-1]
#     for i in vals[::-1]:
#     	next_node = head
#     	head = ListNode(i)
#     	head.next = next_node
#     return head

if __name__ == '__main__':
	print 'hw'