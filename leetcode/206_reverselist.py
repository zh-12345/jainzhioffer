from Linked_list.SingleLinkList import SingleNode, SingleLinkList
class SingleNode():
    def __init__(self,item):
        self.item = item
        self.node = None
class Solution():
    def reverseList(self,head):
        if not head or not head.next:
            return head
        pre = None
        while head:
            pNext = head.next
            head.next = pre
            pre = head
            head = pNext
        return pre
    def travel(self, head):
        # 遍历链表
        cur = head
        while (cur != None):
            print(cur.item, end=' ')
            cur = cur.next
        print("\n")
if __name__ == "__main__":
    h = Solution()
    li = SingleLinkList()
    # print(li.is_empty())
    # print(li.length())
    # i = 0
    # while i < 5:
    #     li.append(i + 1)
    #     i += 1
    li.append(1)
    li.travel()
    result = h.reverseList(li._head)
    h.travel(result)