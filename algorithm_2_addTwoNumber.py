# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        copy = None

        # two non-empty list
        if (l1 != None) and (l2 != None):
            # if there is still one list that have digits
            reply = None
            carry = 0
            while(l1 !=None or l2 != None):
                if (l1 != None):
                    value1 = l1.val
                else:
                    value1 = 0
                if (l2 != None):
                    value2 = l2.val
                else:
                    value2 = 0

                sum = value1 + value2 + carry
                digit = sum % 10
                carry = sum // 10

                if reply == None:
                    reply = ListNode(digit)
                    copy = reply
                else:
                    reply.next = ListNode(digit)
                    reply = reply.next

                if(l1 != None):
                    l1 = l1.next
                if(l2 != None):
                    l2 = l2.next

            # in the end, there might be a carry
            if carry != 0:
                reply.next = ListNode(carry)

            # copy equal to reply?
            return copy

    def addTwoNumbersBetter(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry,10)
            n.next = ListNode(val)
            n = n.next
        return root.next


instance = Solution()

list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(3)

list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)

#reply = instance.addTwoNumbers(list1,list2)
reply = instance.addTwoNumbersBetter(list1,list2)
while(reply != None):
    print(reply.val)
    reply = reply.next