class SingleNode(object):
    """单链表的节点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next 存放下一个节点的标识
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
    def hasCycle(self):
        if self.is_empty() or self._head.next == None:
            return False
        slow = self._head
        fast = slow.next
        while fast != None and fast.next != None:
            if fast == slow:
                return True

            slow = slow.next
            if fast.next:
                fast = fast.next.next
        return False

    # 在链表存在环的情况下找到两者相遇的节点
    # 快慢指针出发点不一致，先到达不同的位置，然后，两个同时出发，会到达环中任意一个节点
    def MeetingNode1(self):
        if self.is_empty() or self._head.next == None:
            return None
        slow = self._head
        fast = slow.next
        while fast != None and fast.next != None:
            if fast == slow:
                return fast

            slow = slow.next
            if fast.next:
                fast = fast.next.next
        return None
    # 快慢指针同时从头结点出发
    def MeetingNode2(self):
        if self.is_empty() or self._head.next == None:
            return None
        slow = self._head
        fast = self._head
        while fast != None and fast.next != None:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            if fast == slow:
                return fast

        return None

    # 关于找到环中节点的个数，所以要要求的相遇节点并不唯一，可以是环中的任意一个节点

    def getCycleNode(self):
        if self.MeetingNode2() is None:
            return
        meetingNode = self.MeetingNode2()
        cur = meetingNode
        count = 1
        while cur.next != meetingNode:
            cur = cur.next
            count += 1
        return count

    # 关于找到环的第一个节点，从头结点到环节点和相遇节点到换节点的距离相同
    def detectCycle(self):
        if self.MeetingNode2() is None:
            return None
        meetingNode = self.MeetingNode2()
        slow = self._head
        fast = meetingNode
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast

        # fast = meetingNode
        # while slow != meetingNode:
        #     slow = slow.next
        #     meetingNode = meetingNode.next
        # return meetingNode

    def detectCycle2(self):
        if self.getCycleNode() is None:
            return
        p1 = self._head
        i = 0
        while i < self.getCycleNode():
            p1 = p1.next
            i += 1
        p2 = self._head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1




if __name__ == "__main__":
    li = SingleHasCycleLinkList()
    li.append(23)
    li.append(34)
    li.append(69)
    li.append(67)
    li.travel()
    li.appendCycleNode(89, 1)
    arr1 = li.MeetingNode2()
    # print(arr1.item)
    # li.add(45)
    # li.travel()
    arr = li.detectCycle2()
    print(arr.item)

    # print(li.getCycleNode())

    # # 这部分测试通过
    # li.append(3)
    # li.append(2)
    # li.append(0)
    # li.append(-4)
    # # li.append(5)
    # # # li.append(6)
    # li.travel()
    # # li.appendCycleNode(6, 2)
    # arr1 = li.MeetingNode2()
    # print(arr1)
    # arr = li.detectCycle()
    # print(arr.item)
