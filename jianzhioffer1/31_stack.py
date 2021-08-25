from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        bPossible =False
        if pushed and popped and len(popped)>0:
            stack = []
            pNextPush=0
            pNextPop=0
            while pNextPop < len(popped):
                while not stack or stack[-1]!=popped[pNextPop]:
                    if pNextPush==len(pushed):
                             break
                    stack.append(pushed[pNextPush])
                    pNextPush +=1
                if stack[-1] != popped[pNextPop]:
                     break
                stack.pop()
                pNextPop +=1
            if not stack and pNextPop==len(popped):
                bPossible =True
        return bPossible
if __name__=='__main__':
    h =Solution()
    pushed=[1, 2, 3, 4, 5]
    popped=[4, 5, 3, 2, 1]
    result= h.validateStackSequences(pushed,popped)
    print(result)