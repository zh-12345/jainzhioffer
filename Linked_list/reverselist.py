from Linked_list.SingleLinkList import SingleNode, SingleLinkList
class Solution:
    # 反转链表
    def reverseList1(self, head):
        if head is None:
            return None

        pPre = None
        while head != None:
            pNext = head.next
            # 切换head的下一个节点，重新指向前一个元素, pre，head 分别向后移
            head.next = pPre
            pPre = head
            head = pNext
        # 至于为什么返回的是pPre，因为pPrey一直继承的是head的值，循环迭代终止也在head
        return pPre

    def reverseList(self, head):

        # 这部分不对，要调整递归条件，head 指向倒数第二个节点
        # head 指向空或者只有一个元素时，就直接返回
        # newhead 则指向对 head的下一个节点调用的递归函数的头节点，此时，newhead 指向最后一个节点
        # 然后 head的下一个节点的next指向head本身，相当于head节点移动到末尾的动作，
        if head is None or head.next is None:
            return head
        newHead = self.reverseList(head.next)
        # 这个问题没有解决是为什么，没有理解这个问题最小的情况是啥，没有考虑只有一个元素的情况
        # 从而这个递归条件就没有设置正确
        # 最小问题的解是什么，就是反转后的头节点返回，同时，直接解决子问题，
        # 回溯法，把head节点移动到末尾，同时最后一个节点为空
        head.next.next = head
        head.next = None
        return newHead
    # 递归的解决，有两个部分
    # 第一个部分，就是对于最基本的情况，也就是问题最小的那种情况，他的解是什么
    # 头部节点后面跟着一个小的短的链表，走早最底的情况，就是链表的头部head为空，也就是整个链表为空
    # 这个也相当于是递归的条件

    # 接下来就是第二个部分，把原问题转换成更小的问题的一个过程
    # 这个头结点后面跟的应该是那个链表中所有的值为val的节点删除后的剩余节点，本来，将问题规模转换成更小的
    # 的问题的时候，就是将链表看成一个头结点后面挂着一个链表，一个头结点后面挂接了一个更短更小的链表，
    # 如果此时这个头结点就是要删的值，那就不要头结点了，直接传回已经删除节点的链表，否则，将头节点和链表连上，传回

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
    i = 0
    while i < 5:
        li.append(i + 1)
        i += 1
    li.travel()
    result = h.reverseList(li._head)
    h.travel(result)
    # print(result.item)

