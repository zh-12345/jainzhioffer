class Queue(object):
    # 队列的话，一般也就几个操作，就是初始化，一个入队，一个出队，判断是否为空，队列成员的个数

    def __init__(self):
        """这个存储队列的数据的容器选择顺序表，这个初始化就是构造函数"""""
        self.__list = []

    def enqueue(self, item):
        self.__list.append(item)

    #     从尾部添加，就从头部弹出，若从头部添加，就从尾部弹出

    def dequeue(self):
        return self.__list.pop(0)

    # 如果经常进行出队操作，就选择在尾部弹出，从头部添加

    def is_empty(self):
        return self.__list() == []

    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    s.enqueue(5)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
