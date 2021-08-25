from typing import List
class SingleNode(object):
    """单链表的节点"""

    def __init__(self, val):
        # val存放数据元素
        self.val = val
        # next 存放下一个节点的标识
        self.next = None


class SingleLinkList():
    # 对象属性
    def __init__(self, node=None):
        # 可以设置默认参数
        self._head = node

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

    def travel(self):
        # 遍历链表
        cur = self._head
        while (cur != None):
            print(cur.val, end=' ')
            cur = cur.next
        print("\n")
    # 使用递归来后序遍历链表
    def travel1(self,head):
        if head is None:
            return

        self.travel1(head.next)
        print(head.val, end=' ')

    # 使用递归来正序遍历链表
    def travel2(self, head):
        if head is None:
            return
        print(head.val, end=' ')
        self.travel2(head.next)


    def add(self, val):
        # 在链表头部插入节点
        node = SingleNode(val)
        node.next = self._head
        self._head = node

    def append(self, val):
        # 在链表尾部插入节点
        # 直接传入数据，用户不需要关心节点信息
        node = SingleNode(val)
        if self.is_empty():
            # 就将链表的_head属性指向node
            self._head = node
        else:
            cur = self._head
            while (cur.next != None):
                cur = cur.next
            cur.next = node

    def insert(self, pos, val):
        # 在链表的任意位置插入节点
        node = SingleNode(val)
        """
        :param pos 起始值从0开始
        i是用来计数的
        """
        if pos <= 0:
            self.add(val)
        elif pos > self.length() - 1:
            self.append(val)
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

    def insert2(self, value, val):
        # 在链表的任意位置插入节点
        node = SingleNode(value)
        """
        :param pos 起始值从0开始
        i是用来计数的
        """
        cur =self._head
        while cur != None:
            if cur.val == val:
                if cur == self._head and not cur.next:
                    cur.next = node
                    break
                else:
                    temp = cur.next
                    cur.next = node
                    node.next = temp
                    break
            else:
                cur = cur.next


    def remove(self, val):
        # 删除某个节点
        # 使用两个游标，一个指向要删除的节点，一个指向要删除节点的前一个节点，也可以直接使用一个游标
        # pre.next = pre.next.next
        cur = self._head
        pre = None
        while (cur != None):
            if cur.val == val:
                # 先判断是否是头结点
                if cur == self._head:
                    self._head = cur.next
                    break
                else:
                    pre.next = cur.next
                    break
            else:
                pre = cur
                cur = cur.next

    # 用递归的方法删除元素
    def removeelemnts(self,phead, val):
        if phead is None:
            return phead
        # 递归的解决，有两个部分
        # 第一个部分，就是对于最基本的情况，也就是问题最小的那种情况，他的解是什么
        # 头部节点后面跟着一个小的短的链表，走早最底的情况，就是链表的头部head为空，也就是整个链表为空
        # 这个也相当于是递归的条件

        # 接下来就是第二个部分，把原问题转换成更小的问题的一个过程
        # 这个头结点后面跟的应该是那个链表中所有的值为val的节点删除后的剩余节点，本来，将问题规模转换成更小的
        # 的问题的时候，就是将链表看成一个头结点后面挂着一个链表，一个头结点后面挂接了一个更短更小的链表，
        # 如果此时这个头结点就是要删的值，那就不要头结点了，直接传回已经删除节点的链表，否则，将头节点和链表连上，传回
        phead.next = self.removeelemnts(phead.next, val)
        if phead.val == val:
            return phead.next
        else:
            return phead






    def search(self, val):
        # 搜寻某个节点是否存在
        cur = self._head
        while (cur != None):
            if cur.val == val:
                return True
            else:
                cur = cur.next
        #     若是最后没有找到，则直接返回假值
        return False

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
        return cur.val

    def deleteAtIndex(self, pos) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        index是从0开始的,一旦使用索引，就需要判断这个索引是否合法
        """
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

    def appendSameNode(self, node):
        # node = SingleNode(val)
        if self.is_empty():
            # 就将链表的_head属性指向node
            self._head = node
        else:
            cur = self._head
            while (cur.next != None):
                cur = cur.next
            cur.next = node

    def deleteDuplicates(self, head: SingleNode) -> SingleNode:
        if not head or not head.next:
            return head
        dummy = SingleNode(0)
        dummy.next = head
        cur = head
        preNode = None
        while cur:

            needDelete = False
            if cur.next and cur.next.val == cur.val:
                needDelete = True
            if not needDelete:
                preNode = cur
                cur = cur.next
            else:
                value = cur.val
                while cur.next and cur.val == value:
                    cur = cur.next
                if not preNode:
                    self._head = cur
                else:
                    preNode.next = cur.next



if __name__ == "__main__":
    li = SingleLinkList()
    li.append(1)
    li.append(1)
    li.append(2)
    li.append(2)
    # li.append(3)
    # li.append(3)
    li.travel()
    li.deleteDuplicates(li._head)
    li.travel()

