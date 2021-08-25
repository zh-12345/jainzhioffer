from Linked_list.SingleLinkList import SingleNode, SingleLinkList
class Solution:

    def FindFirstCommenNode(self, headA, headB):
        #     得到链表的长度
        nlength1 = self.length(headA)
        print(nlength1)
        nlength2 = self.length(headB)
        print(nlength2)



        p1 = headA
        p2 = headB
          # #     然后两个链表对齐
        while nlength1 < nlength2:
            p2 = p2.next
            nlength2 -= 1
        while nlength2 < nlength1:
            p1 = p1.next
            nlength1 -= 1

        while p1 and p2  and p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1


    def FindFirstCommenNode1(self, headA, headB):
        #     得到链表的长度
        nlength1 = self.length(headA)
        print(nlength1)
        nlength2 = self.length(headB)
        print(nlength2)

        A, B = headA, headB
        # 尾节点最后还有个空节点
        # 换的思想在于什么，距离相等，总会相遇
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

    def FindFirstCommenNode2(self, headA, headB):
        stack1 = []
        stack2 = []
        head1, head2 = headA, headB
        while head1:  # 将第一个链表的节点依次放入第一个栈中
            stack1.append(head1)
            head1 = head1.next
        while head2:  # 将第二个链表的节点依次放入第二个栈中
            stack2.append(head2)
            head2 = head2.next
        node = SingleNode(None)
        # 从两个栈顶开始，依次比较，找到最后一个相等的节点
        while stack1 and stack2 and stack1[-1] is stack2[-1]:
            node = stack1.pop()
            stack2.pop()
        return node  # 返回公共节点的值







    def length(self,phead):
        # 链表的长度
        cur = phead
        count = 0
        while (cur != None):
            count += 1
            cur = cur.next
        return count


if __name__ == "__main__":
    h = Solution()
    li = SingleLinkList()
    node1 = SingleNode(6)
    node2 = SingleNode(7)
    li.append(2)
    li.append(3)
    li.appendSameNode(node1)
    li.appendSameNode(node2)
    # li.append(6)
    # li.append(7)
    li.add(1)
    li.travel()
    li2 = SingleLinkList()
    li2.append(5)
    li2.appendSameNode(node1)
    # li2.appendSameNode(node2)
    # li2.append(6)
    # li2.append(7)
    li2.add(4)
    li2.travel()

    # result = h.FindFirstCommenNode(li._head, li2._head)
    result = h.FindFirstCommenNode1(li._head, li2._head)
    # result = h.FindFirstCommenNode(li, li2)
    # result = h.FindFirstCommenNode2(li._head, li2._head)
    print(result.item)
