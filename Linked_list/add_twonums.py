from Linked_list.SingleLinkList import SingleNode, SingleLinkList


class Solution:
    def addTwoNumbers(self, l1, l2) :
        # 最重要的是创建一个新的链表，一个链表最关键的就是头节点
        # 最好保持头结点不要变，先给定一个头结点，然后再在这个节点上挂新的节点
        dummy = SingleNode(0)
        cur = dummy
        carry = 0
        while l1 != None or l2 != None:
            # 加法的原理 就是个位数相加同时还要加上进位，
            # 还有一点需要注意，如果最高位也需要进位，还需要再加上一个值为1的节点
            l1_value = l1.item if l1 else 0
            l2_value = l2.item if l2 else 0
            summery = l1_value + l2_value + carry
            carry = summery // 10
            cur.next = SingleNode(summery % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            cur.next = SingleNode(1)
        return dummy.next


    def travel(self,head):
        cur = head
        while cur != None:
            print(cur.item, end=' ')
            cur = cur.next


if __name__ == "__main__":
    h = Solution()
    li = SingleLinkList()
    ki = SingleLinkList()
    li.append(2)
    li.append(4)
    li.append(3)
    ki.append(5)
    ki.append(6)
    ki.append(4)
    result = h.addTwoNumbers(li._head, ki._head)
    h.travel(result)