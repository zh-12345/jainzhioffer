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
    #    self.__list.pop(0)
    def peak(self):
        """返回栈顶元素"""
        """顺序表的最后一个元素"""
        if self.__list:
           return self.__list[-1]
        else:
            return None

    def  is_empty(self):
        """判断栈是否为空"""
        """直接判断该顺序表是不是为空"""
        return self.__list==[]

    def size(self):
        """返回栈的元素"""
        return len(self.__list)



class Solution():
    def isValid(self,s):
        if len(s)<0:
            return False
        a = Stack()
        for ss in s:
            if ss == '(' or ss =='[' or ss =='{':
                a.push(ss)
            else:
                if a.is_empty():
                    return False
                if ss == ')' and a.peak() != '(':
                    return False
                if ss == ']' and a.peak() != '[':
                    return False
                if ss == '}' and a.peak() != '{':
                    return False
                a.pop()
        return a.is_empty()

    def isValid2(self, s):
        if len(s)<0 or len(s)%2 ==1:
            return False
        stack = list()
        pair= {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for ss in s:
            if ss in pair:
                if not stack or stack[-1] != pair[ss]:
                    return False
                stack.pop()
            else:
                stack.append(ss)
        return not stack
if __name__ =="__main__":
    h= Solution()
    s = '([)]'
    print(h.isValid2(s))
