class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class MyLinkedList:

    def __init__(self,node=None):
        """
        Initialize your data structure here.
        """
        self.__head = node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        找到对应索引的
        """
        if index < 0 or index >= self.length():
            return -1
        if self.is_empty():
            return -1
        cur = self.__head
        i = 0
        while (i < index):
            i += 1
            cur = cur.next
        return cur.item

    def length(self):
        # 链表的长度
        cur = self.__head
        count = 0
        while (cur != None):
            count += 1
            cur = cur.next
        return count

    def is_empty(self):
        # 判断链表是否为空
        return self.__head is None

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.__head
        self.__head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while (cur.next != None):
                cur = cur.next
            cur.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = Node(val)
        if index <= 0:
            self.addAtHead(val)
        elif index > self.length() - 1:
            self.addAtTail(val)
        else:
            i = 0
            p = self.__head
            while (i < index - 1 and p != None):
                i += 1
                p = p.next
            node.next = p.next
            p.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length():
            return False
        if self.is_empty():
            return False
        i = 0
        p = self.__head
        if index == 0:
            self.__head = p.next
        else:
            while (p != None and i < index - 1):
                p = p.next
                i += 1
            p.next = p.next.next

    def travel(self):
        # 遍历链表
        cur = self.__head
        while (cur != None):
            print(cur.item, end=' ')
            cur = cur.next
        print("\n")

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtIndex(0,10)
obj.travel()
obj.addAtIndex(0,20)
obj.travel()
obj.addAtIndex(1,30)
obj.travel()

