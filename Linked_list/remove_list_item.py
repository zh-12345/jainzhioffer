from Linked_list.SingleLinkList import SingleNode, SingleLinkList


class Solution:

    # 这个方法在于通不过是因为遍历链表两次了，不符合题目要求
    # global mm
    def __init__(self):
        self.i = 0

    def removeNthFromEnd2(self, head: SingleNode, n: int) -> SingleNode:
        pos = self.length(head) - n
        if pos < 0 or pos >= self.length(head):
            return False
        if head is None:
            return False
        i = 0
        p = head
        if n == 0:
            head = p.next
        else:
            while (p != None and i < pos - 1):
                p = p.next
                i += 1
            p.next = p.next.next

    def removeNthFromEnd3(self, head: SingleNode, n: int) -> SingleNode:
        if head is None:
            return
        pre, cur = head, head
        i = 0
        while i < n:
            cur = cur.next
            i += 1
        if cur is None:
            head = head.next
        while cur != None and cur.next != None:
            cur = cur.next
            pre = pre.next
        pre.next = pre.next.next

    # 尝试用递归来解决问题
    def removeNthFromEnd(self, head: SingleNode, n: int) -> SingleNode:
        global mm
        mm = 0
        # 递归的解决，有两个部分
        # 第一个部分，就是对于最基本的情况，也就是问题最小的那种情况，他的解是什么
        # 头部节点后面跟着一个小的短的链表，走早最底的情况，就是链表的头部head为空，也就是整个链表为空
        # 这个也相当于是递归的条件

        # 接下来就是第二个部分，把原问题转换成更小的问题的一个过程
        # 这个头结点后面跟的应该是那个链表中所有的值为val的节点删除后的剩余节点，本来，将问题规模转换成更小的
        # 的问题的时候，就是将链表看成一个头结点后面挂着一个链表，一个头结点后面挂接了一个更短更小的链表，
        # 如果此时这个头结点就是要删的值，那就不要头结点了，直接传回已经删除节点的链表，否则，将头节点和链表连上，传回
        if head is None:
            mm = 0
            return None
        head.next = self.removeNthFromEnd(head.next, n)
        mm += 1
        # 如果计数刚好到头节点，那么就返回移除好的剩余节点，否则，就将头结点和链表连上，传回
        return head.next if mm == n else head




    def length(self, head):
        # 链表的长度
        cur = head
        count = 0
        while (cur != None):
            count += 1
            cur = cur.next
        return count


if __name__ == "__main__":
    h = Solution()
    li = SingleLinkList()
    # print(li.is_empty())
    # print(li.length())
    i = 0
    while i < 5:
        li.append(i + 1)
        i += 1
    li.travel()
    # h.removeNthFromEnd(li._head, 2)
    h.removeNthFromEnd(li._head, 2)
    li.travel()
