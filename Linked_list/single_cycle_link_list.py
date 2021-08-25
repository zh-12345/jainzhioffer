class SingleNode(object):
    """单链表的节点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next 存放下一个节点的标识
        self.next = None

class SingleCycleLinkList():
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
        if self.is_empty():
            return 0
        cur = self._head
        count = 1
        # 循环停止条件与之前的
        while (cur.next != self._head):
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历链表
        if self.is_empty():
            return
        cur = self._head
        while (cur.next != self._head):
            print(cur.item, end=' ')
            cur = cur.next
        # 退出循环，cur指向了尾节点
        print(cur.item)
        # print("\n")

    def add1(self, item):
        # 在链表头部插入节点,不仅需要头结点指向，还需要遍历找到尾节点，然后将尾节点指向头结点
        # 先打断再进行遍历找到尾节点
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
            node.next = node
        # else:
        #     node.next = self._head
        #     if self.length() == 1:
        #         node.next.next = node
        #         self._head = node
        #         return
        #     else:
        #         cur = self._head
        #         self._head = node
        #         while(cur.next != node.next):
        #             cur = cur.next
        #         cur.next = node
        else:
            node.next = self._head
            cur = self._head
            self._head = node
            while(cur.next != node.next):
                cur = cur.next
            cur.next = node

    def add(self, item):
        # 在链表头部插入节点,不仅需要头结点指向，还需要遍历找到尾节点，然后将尾节点指向头结点
        # 先找到尾节点
        node = SingleNode(item)
        # 判断是不是空
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while (cur.next != self._head):
                cur = cur.next
            node.next = self._head
            self._head = node
            cur.next = node

    def append(self, item):
        # 在链表尾部插入节点
        # 直接传入数据，用户不需要关心节点信息
        node = SingleNode(item)
        if self.is_empty():
            # 就将链表的__head属性指向node
            self._head = node
            node.next = node
        else:
            cur = self._head
            while (cur.next != self._head):
                cur = cur.next
            node.next = self._head
            cur.next = node
#           若是先操作cur
#           cur.next = node
#           node.next = self._head
    def insert(self, pos, item):
        # 在链表的任意位置插入节点
        # 这部分与单链表完全一致，因为它主要是在中间插入的，所以不涉及头尾部节点的变化
        node = SingleNode(item)
        """
        :param pos 起始值从0开始
        i是用来计数的
        """
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1 :
            self.append(item)
        else:
            i = 0
            p = self._head
            while (p != None and i < pos - 1):
                p = p.next
                i += 1
            # if(i > pos-1 or p == None):
            #     return False
            node.next = p.next
            p.next = node

    def search(self, item):
        # 搜寻某个节点是否存在,查找就是遍历，遍历就要观察条件了
        if self.is_empty():
            return False
        cur = self._head
        while(cur.next != self._head):
            if cur.item == item:
                return True
            else:
                cur = cur.next
    #     若是最后没有找到，则直接返回假值
    #     这里退出循环的时候，指向了尾节点，尾节点没有进入到循环，没有进行下一步的判断，需要重新处理尾节点
        if cur.item == item:
            return True
        return False

    def remove(self, item):
        # 删除某个节点
        # 使用两个游标，一个指向要删除的节点，一个指向要删除节点的前一个节点，也可以直接使用一个游标
        # pre.next = pre.next.next
        if self.is_empty():
            return
        cur = self._head
        pre = None
        while(cur.next != self._head):
            if cur.item == item:
                # 先判断是否是头结点，需要找到尾部节点，重新指向
                if cur == self._head:
                    # 开始找尾节点，需要设置一个新的游标
                    rear = self._head
                    while(rear.next != self._head):
                        rear = rear.next
                    self._head = cur.next
                    rear.next = self._head
                    return
                else:
                    # 中间节点
                    pre.next = cur.next
                    return
            else:
                pre = cur
                cur = cur.next
#         退出循环体，要单独判断尾节点
        if cur.item == item:
            # if self.length() == 1:
            if cur == self._head:
            #     链表只有一个节点
                self._head = None
            else:
                pre.next = cur.next


if __name__ == "__main__":
    li = SingleCycleLinkList()
    # li.add(34)
    # li.travel()
    # li.add(45)
    # li.travel()
    # li.add(56)
    # li.travel()
    # print(li.length())
    # li.add1(34)
    # # print(li.length())
    # # li.travel()
    # li.add1(45)
    # li.travel()
    li.append(34)
    li.add1(56)
    # li.travel()
    li.append(67)
    # # li.add1(56)
    # li.travel()
    # li.append(88)
    # # li.add1(56)
    # li.travel()
    # li.insert(3,23)
    # # li.add1(56)
    li.travel()
    # print(li.search(34))
    print("开始移除")
    li.remove(56)
    li.travel()