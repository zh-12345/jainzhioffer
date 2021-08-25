class DoubleQueue(object):
    # 用顺序表来实现
    def  __init__(self):
        self.__list = []

    def deque(self):
        pass

    def add_front(self,item):
        # 本意上双端队列的头和列表的头没有啥关系，这里使用双端的头为列表的头
        self.__list.insert(0,item)

    def add_rear(self,item):
        self.__list.append(item)

    def pop_front(self):
        return self.__list.pop(0)

    def pop_rear(self):
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

if __name__ == "__main__":
    s = DoubleQueue()
    s.add_front(1)
    s.add_front(2)
    s.add_rear(3)
    s.add_rear(4)
    # print(s.pop_front())
    # print(s.pop_front())
    # print(s.pop_front())
    # print(s.pop_front())
    print(s.pop_rear())
    print(s.pop_rear())
    print(s.pop_rear())
    print(s.pop_rear())