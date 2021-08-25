class  Stack(object):
    """栈"""
    """可以用顺序表，也可以用链表才存储数据"""
    def __init__(self):
        self.__list=[]

    def push(self,item):
        """压栈"""
        self.__list.append(item)
    #   self.__list.insert(0,item)
    """如果使用顺序表的话，可以选择在头部或者是尾部作为栈的出入口，如果在头部的话，时间复杂度是O(n),尾部的时间复杂度是O(1)"""
    def pop(self):
        """出栈"""
        return self.__list.pop()
class CQueue:

    def __init__(self):
        self.stack1,self.stack2 = [],[]

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if len(self.stack2) <= 0:
            while len(self.stack1) > 0:
                data = self.stack1.pop()
                self.stack2.append(data)
        if len(self.stack2) == 0:
            return -1
        return self.stack2.pop()

if __name__ == "__main__":
    obj = CQueue()
    print(obj)
    obj.appendTail(3)
    print(obj)
    print(obj.deleteHead())
    print(obj.deleteHead())