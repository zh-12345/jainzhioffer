class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.listA=[]
        self.listB=[]


    def push(self, x: int) -> None:
        self.listA.append(x)
        if not self.listB or x < self.listB[-1]:
            self.listB.append(x)
        else:
            self.listB.append(self.listB[-1])



    def pop(self) -> None:
        self.listA.pop()
        self.listB.pop()


    def top(self) -> int:
        if self.listA:
            return self.listA[-1]
        else:
            return None


    def min(self) -> int:
        return self.listB[-1] if self.listB else None


if __name__=='__main__':
    h =MinStack()
    h.push(-2)
    h.push(0)
    h.push(-1)
    print(h.min())
    print(h.top())
    h.pop()
    print(h.min)
