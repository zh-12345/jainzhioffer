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

        while p1 != None and p2 != None and p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
        # cur1 = headA
        # cur2 = headB
        # n = 0
        # while cur1:
        #     n += 1
        #     cur1 = cur1.next
        # while cur2:
        #     n -= 1
        #     cur2 = cur2.next
        # if cur1 != cur2:
        #     return None
        # cur1 = headA if n > 0 else headB
        # cur2 = headB if cur1 == headA else headA
        # n = abs(n)
        # while n:
        #     n -= 1
        #     cur1 = cur1.next
        # while cur1 != cur2:
        #     cur1 = cur1.next
        #     cur2 = cur2.next
        # return cur1



    def length(self,phead):
        # 链表的长度
        cur = phead
        count = 0
        while (cur != None):
            count += 1
            cur = cur.next
        return count


    def printLinkedList(self,head):
        while head:
            print(head.item, end=" ")
            head = head.next
        print()

    def travel(self,head):
        # 遍历链表
        cur = head
        while (cur != None):
            print(cur.item, end=' ')
            cur = cur.next
        print("\n")

if __name__ == "__main__":
    h = Solution()
    head1 = SingleNode(0)
    node1, node2, node3, node4, node5 = SingleNode(1), SingleNode(4), SingleNode(6), SingleNode(7), SingleNode(8)
    head1.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # h.travel(head1)
    h.printLinkedList(head1.next)

    head2 = SingleNode(0)
    node6, node7 = SingleNode(2), SingleNode(3)
    head2.next = node6
    node6.next = node7
    node7.next = node4
    h.printLinkedList(head2.next)
    result = h.FindFirstCommenNode(head1.next,head2.next)
    print(result.item)



