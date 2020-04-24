class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        rtype = ListNode(0)
        rtemp = rtype
        carry = 0
        while (l1 or l2):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sumNum = val1 + val2 + carry
            rtemp.next = ListNode(sumNum % 10)
            carry = sumNum // 10
            rtemp = rtemp.next
            if (l1 != None):
                l1 = l1.next
            if (l2 != None):
                l2 = l2.next
        if (carry > 0):
            rtemp.next = ListNode(1) 
        return rtype.next

if __name__ == "__main__":
    # Test Cases
    l1 = ListNode([2,4,3])
    l2 = ListNode([5,6,4])
    print(Solution().addTwoNumbers(l1,l2))

