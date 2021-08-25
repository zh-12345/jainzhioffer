class SingleNode(object):
    def __init__(self,item):
        self.item = item
        self.next = None
class SingleLinkList():
    # 对象属性
    def __init__(self, node=None):
        # 可以设置默认参数
        self._head = node

    def is_empty(self):
        # 判断链表是否为空
        return self._head is None

    def travel(self):
        # 遍历链表
        cur = self._head
        while (cur != None):
            print(cur.item, end=' ')
            cur = cur.next
        print("\n")


    def append(self, item):
        # 在链表尾部插入节点
        # 直接传入数据，用户不需要关心节点信息
        node = SingleNode(item)
        if self.is_empty():
            # 就将链表的_head属性指向node
            self._head = node
        else:
            cur = self._head
            while (cur.next != None):
                cur = cur.next
            cur.next = node
    def length(self):
        # 链表的长度
        cur = self._head
        count = 0
        while (cur != None):
            count += 1
            cur = cur.next
        return count

    def deleteAtIndex1(self, pos) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        index是从0开始的,一旦使用索引，就需要判断这个索引是否合法
        """
        pos = self.length() - pos
        if pos < 0 or pos >= self.length():
            return False
        if self.is_empty():
            return False
        i = 0
        p = self._head
        if pos == 0:
            self._head = p.next
        else:
            while (p != None and i < pos - 1):
                p = p.next
                i += 1
            p.next = p.next.next

    def removeNthFromEnd(self,head,n):

        if not head:
            return head
        length = self.length1(head)
        n = length - n
        if n < 0 or n >= length:
            return head

        i = 0
        p = head
        if n == 0:
            head = p.next
        else:
            while p and i < n - 1:
                p = p.next
                i += 1
            p.next = p.next.next

    def length1(self, head):
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def removeNthFromEnd2(self, head, n):
        if not head:
            return head
        cur,pre = head,head
        for i in range(n):
            cur =cur.next
        if not cur :
            return head.next
        while cur.next:
            cur = cur.next
            pre = pre.next
        pre.next = pre.next.next


if __name__ == "__main__":
    li = SingleLinkList()
    li.append(1)
    li.append(2)
    li.append(3)
    li.append(4)
    li.append(5)
    li.travel()
    li.removeNthFromEnd2(li._head,2)
    li.travel()

