from Linked_list.SingleLinkList import SingleLinkList


class Node(object):
    """双向链表的节点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        self.next = None
        self.pre = None


class DoubleLinkList(SingleLinkList):
    # 对象属性
    def __init__(self, initialize=None):
        # 可以设置默认参数
        node=Node(initialize)
        super().__init__(node)

    #
    # def is_empty(self):
    #     # 判断链表是否为空
    #     return self.head is None
    #
    # def length(self):
    #     # 链表的长度
    #     cur = self.head
    #     count = 0
    #     while (cur != None):
    #         count += 1
    #         cur = cur.next
    #     return count
    #
    # def travel(self):
    #     # 遍历链表
    #     cur = self.head
    #     while (cur.item != None):
    #         print(cur.item, end=' ')
    #         cur = cur.next
    #     print("\n")

    def add(self, item):
        # 在链表头部插入节点
        node = Node(item)
        node.next = self.head
        self.head = node
        node.next.pre = node

    def append(self, item):
        # 在链表尾部插入节点
        node = Node(item)
        # 先判断是不是为空链表，如果为空，直接把头结点指向node
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while (cur.next != None):
                cur = cur.next
            cur.next = node
            node.pre = cur

    # def insert(self, pos, item):
    #     # 在链表的任意位置插入节点
    #
    #
    # def remove(self, item):
    #
    #
    # def search(self, item):
    #     # 搜寻某个节点是否存在
    #
    #
    # def get(self, index):
    #     """
    #     Get the value of the index-th node in the linked list. If the index is invalid, return -1.
    #     找到对应索引的节点值
    #     """
    #
    #
    # def deleteAtIndex(self, pos) -> None:
    #     """
    #     Delete the index-th node in the linked list, if the index is valid.
    #     index是从0开始的,一旦使用索引，就需要判断这个索引是否合法
    #     """


if __name__ == "__main__":
    li = DoubleLinkList()
    li.append(23)
    li.append(78)
    li.add(89)
    li.add(67)
    li.travel()
