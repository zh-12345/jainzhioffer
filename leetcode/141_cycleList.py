class SingleNode():
    def __init__(self,item):
        self.item = item
        self.next = None
class SingleHasCycleLinkList():
    # 对象属性
    def __init__(self, node=None):
        # 可以设置默认参数
        self._head = node
        if node:
            # 判断如果不是空的，就将自己给自己挂上去
            node.next = node

    def is_empty(self):
        # 判断链表是否为空
        return self._head is None

    def length(self):
        # 链表的长度
        cur = self._head
        count = 0
        while (cur != None):
            count += 1
            cur = cur.next
        return count

    def add(self, item):
        # 在链表头部插入节点
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        # 在链表尾部插入节点
        # 直接传入数据，用户不需要关心节点信息
        node = SingleNode(item)
        if self.is_empty():
            # 就将链表的__head属性指向node
            self._head = node
        else:
            cur = self._head
            while (cur.next != None):
                cur = cur.next
            cur.next = node

    def travel(self):
        # 遍历链表
        cur = self._head
        while (cur != None):
            print(cur.item, end=' ')
            cur = cur.next
        print("\n")

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        找到对应索引的节点值
        """
        if index < 0 or index >= self.length():
            return False
        if self.is_empty():
            return False
        cur = self._head
        i = 0
        while (i < index):
            i += 1
            cur = cur.next
        return cur

    # 这个添加好像不合理，因为我传的参的是新值，重新形成一个新节点
    def appendCycleNode(self, item, index):
        node = SingleNode(item)
        if self.is_empty():
            # 就将链表的__head属性指向node
            self._head = node
            node.next = node
        else:
            cur = self._head
            while (cur.next != None):
                cur = cur.next
            cur.next = node
            pointnode = self.get(index)
            node.next = pointnode

    # 此为判断
    def hasCycle(self,head):
        if not head or not head.next:
            return False
        slow = head
        fast = slow.next
        while fast and fast.next:
            if fast == slow:
                return True

            slow = slow.next
            if fast.next:
                fast = fast.next.next
        return False

if __name__ == "__main__":
    li = SingleHasCycleLinkList()
    li.append(23)
    li.append(34)
    li.append(69)
    li.append(67)
    li.travel()
    li.appendCycleNode(89, 1)
    print(li.hasCycle(li._head))
    # arr1 = li.MeetingNode2()
    # # print(arr1.item)
    # # li.add(45)
    # # li.travel()
    # arr = li.detectCycle2()
    # print(arr.item)