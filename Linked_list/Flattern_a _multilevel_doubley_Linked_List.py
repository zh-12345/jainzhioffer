class Node(object):
    """多层双向链表的节点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        self.next = None
        self.prev = None
        self.child = None


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        pre = None
        self.recursive(head, pre)
        return head

    def recursive(self,head, pre):
            if head is None:
                return
            child = head.child
            next1 = head.next
            if pre:
                pre.next = head
                head.prev = pre
                pre.child = None
            pre = head
            self.recursive(child, pre)
            self.recursive(next1, pre)



    def travel(self, head):
        cur = head
        while cur != None:
            print(cur.item, end=' ')
            cur = cur.next
        print('\n')


if __name__ == "__main__":
    h = Solution()
    node1 = Node(1)
    head = node1
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)
    node1.next = node2
    node2.next = node3
    node2.prev = node1
    node3.next = node4
    node3.prev = node2
    node3.child = node7
    node4.next = node5
    node4.prev = node3
    node5.next = node4
    node5.prev = node4
    node6.prev = node5
    node7.next = node8
    node8.next = node9
    node8.prev = node7
    node8.child = node11
    node9.next = node10
    node9.prev = node8
    node10.prev = node9
    node11.next = node12
    node12.prev = node11
    result = h.flatten(head)
    h.travel(result)
