class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1, self.queue2 = [], []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.queue2) <= 0:
          while len(self.queue1) > 1:
              data = self.queue1.pop(0)
              self.queue2.append(data)
          return self.queue1.pop(0)
        if len(self.queue1) <= 0:
          while len(self.queue2) > 1:
              data = self.queue2.pop(0)
              self.queue1.append(data)
          return self.queue2.pop(0)
        if len(self.queue1) == 0 and len(self.queue2)==0:
            return -1

    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.queue1) == 0 and len(self.queue2)==0:
            return -1
        elif len(self.queue1) == 0 :
            return self.queue2[-1]
        else :
            return self.queue1[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            return True
        return False

if __name__ =='__main__':
   obj = MyStack()
   obj.push(1)
   print(obj)
   obj.push(2)

   print(obj.top())
   print(obj.pop())
   print(obj.pop())
   print(obj.empty())