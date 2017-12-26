#1562 / 1562 test cases passed.

#Runtime: 122 ms

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head_node = current_node = ListNode(-1)
        previous_carry = 0
        
        while (l1 or l2):
              
            if l2 is not None and l1 is not None:             #if we are at the same place in both numbers
                carry = (l1.val + l2.val + previous_carry) / 10
                digit_sum = (l1.val + l2.val + previous_carry) % 10
                previous_carry = carry
                l1 = l1.next
                l2 = l2.next

            elif l2 is None and l1 is not None:               #if the first number is larger in size than the second number
                carry = (l1.val + previous_carry) / 10
                digit_sum = (l1.val + previous_carry) % 10
                previous_carry = carry
                l1 = l1.next

            elif l1 is None and l2 is not None:               #if the second number is larger in size than the first number
                carry = (l2.val + previous_carry) / 10
                digit_sum = (l2.val + previous_carry) % 10
                previous_carry = carry
                l2 = l2.next
                     
            current_node.next = ListNode(digit_sum)           #creating the next node and shifting the current pointer to the new node
            current_node = current_node.next
        
        if previous_carry:                                    #creating a new node for the last carry if it is 1
            current_node.next = ListNode(previous_carry)           
            current_node = current_node.next 
        
        #both numbers have been fully traversed
        return head_node.next     
