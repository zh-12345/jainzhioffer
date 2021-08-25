from Linked_list.SingleLinkList import SingleNode, SingleLinkList


class Solution:
    def mergeTwoLists(self, l1, l2):
        # 由于两个链表的长度可能不同，所以最终会有一个链表先完成插入所有的元素，
        # 直接另一个没有完成的链表直接链入新链表的结尾
        if l1 is None:
            #             虽然返回的是一个头节点，其实是一个已经完成合并任务的链表
            return l2
        elif l2 is None:
            return l1
        pMergeHead = None
        if l1.item < l2.item:
            pMergeHead = l1
            pMergeHead.next = self.mergeTwoLists(l1.next, l2)
        else:
            pMergeHead = l2
            pMergeHead.next = self.mergeTwoLists(l1, l2.next)
        return pMergeHead

    def travel(self, head):
        cur = head
        while cur != None:
            print(cur.item, end=' ')
            cur = cur.next


if __name__ == "__main__":
    h = Solution()
    li = SingleLinkList()
    ki = SingleLinkList()
    # li.append(2)
    # li.append(3)
    i = 0
    while i < 8:
        li.append(i + 1)
        i += 2
    i = 1
    while i < 9:
        ki.append(i + 1)
        i += 2
    li.travel()
    ki.travel()
    result = h.mergeTwoLists(li._head, ki._head)
    h.travel(result)
