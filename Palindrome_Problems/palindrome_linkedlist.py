from Linked_list.SingleLinkList import SingleNode, SingleLinkList


class Solution:
    def isPalindrome1(self, head):
        # 一个元素也称之为回文列表
        if head is None:
            return False
        phead = head
        cur = head
        stack = []
        while phead:
            stack.append(phead)
            phead = phead.next
        while cur != None and stack and stack[-1].item == cur.item:
            stack.pop()
            cur = cur.next
        if cur != None and stack:
            return False
        return True

    def isPalindrome2(self, head):
        def check(head):
            if head is None:
                return
            check(head.next)
            if head.item != self.temp.item:
                self.res = False
            self.temp = self.temp.next

        self.temp = head
        # 如果这个值不设为真的话，他走出循环就会是原始值
        self.res = True
        check(head)
        return self.res

    def isPalindrome3(self, head):
        fast, slow = head, head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        if fast != None:
            slow = slow.next

        #         slow 代表的是回文链表的开始
        def reverse(head):

            #         为了降低空间复杂度，暂时不使用递归来处理问题
            pre = None
            pNode = head
            while pNode != None:
                pNext = pNode.next
                pNode.next = pre
                pre = pNode
                pNode = pNext
            return pre
#           开始比较，此时我们需要先反转后半部分链表
        left = head
        right = reverse(slow)
        while right != None:
            if left.item != right.item:
                return False
            left = left.next
            right = right.next
        return True
if __name__ == "__main__":
    h = Solution()
    li = SingleLinkList()
    # li.append(2)
    # li.append(3)
    i = 0
    while i < 5:
        li.append(i + 1)
        i += 1
    while i > 1:
        li.append(i)
        i -= 1
    li.travel()
    print(h.isPalindrome3(li._head))
