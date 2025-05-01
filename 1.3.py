class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr and curr.next:
            if curr.val > curr.next.val:
                prev = dummy
                while prev.next and prev.next.val < curr.next.val:
                    prev = prev.next
                temp = curr.next
                curr.next = curr.next.next
                temp.next = prev.next
                prev.next = temp
            else:
                curr = curr.next
        
        return dummy.next
