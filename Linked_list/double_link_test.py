# from Linked_list.SingleLinkList import SingleLinkList


class Node(object):
    """双向链表的节点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        self.next = None
        self.pre = None


class DoubleLinkList(object):
    # 对象属性
    def __init__(self, node=None):
        # 可以设置默认参数
        self.__head = node

    #
    def is_empty(self):
        # 判断链表是否为空
        return self.__head is None

    def length(self):
        # 链表的长度
        cur = self.__head
        count = 0
        while (cur != None):
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历链表
        cur = self.__head
        while (cur != None):
            print(cur.item, end=' ')
            cur = cur.next
        print("\n")

    def add(self, item):
        # 在链表头部插入节点
        node = Node(item)

        node.next = self.__head
        self.__head = node

        if node.next:
            node.next.pre = node

    def append(self, item):
        # 在链表尾部插入节点
        node = Node(item)
        # 先判断是不是为空链表，如果为空，直接把头结点指向node
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while (cur.next != None):
                cur = cur.next
            cur.next = node
            node.pre = cur

    def insert(self, pos, item):
        # 在链表的任意位置插入节点
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            #     之前在单向链表中指定位置插入某个节点，需要两个游标，现在双向链表，不需要指定位置的前一个节点位置
            count = 0
            cur = self.__head
            while count < pos:
                count += 1
                cur = cur.next
            node.next = cur
            node.pre = cur.pre
            cur.pre.next = node
            cur.pre = node

    def remove(self, item):
        cur = self.__head
        while (cur != None):
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        # 判断是否只有一个节点
                        cur.next.pre = None
                else:
                    cur.pre.next = cur.next
                    if cur.next:
                        cur.next.pre = cur.pre
                break
            else:
                cur = cur.next

    def search(self, item):
        #     # 搜寻某个节点是否存在
        # 遍历判断是否相等
        cur = self.__head
        while (cur != None):
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        找到对应索引的节点值
        确定索引合法
        """
    #
    #
    # def deleteAtIndex(self, pos) -> None:
    #     """
    #     Delete the index-th node in the linked list, if the index is valid.
    #     index是从0开始的,一旦使用索引，就需要判断这个索引是否合法
    #     """


if __name__ == "__main__":
    li = DoubleLinkList()
    # li.append(45)
    # li.append(78)
    li.add(23)
    li.travel()
    li.insert(5, 56)
    li.travel()
    print("移除")
    li.remove(23)
    li.travel()
