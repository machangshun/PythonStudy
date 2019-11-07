class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution(object):
    def addTwoNumbers(self,l1,l2):
        pass



if __name__ == '__main__':
    ans = Solution()
    l1 = ListNode(1)
    l1.next = 1
    l2 = ListNode(2)
    l2.next = 1
    ans.addTwoNumbers(l1,l2)
