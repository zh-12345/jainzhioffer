from typing import List
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = []
        if n <= 0:
            return res
        number = ['0' for i in range(n)]

        def dfs(x):
            if x == n:
                s = ''.join(number[self.start:])
                if s != '0':
                    res.append(int(s))
                if n - self.start == self.nine:
                    self.start -= 1
                return
            for i in range(10):
                if i == 9:
                    self.nine += 1
                number[x] = str(i)
                dfs(x + 1)
            self.nine -= 1

        self.nine = 0
        self.start = n - 1
        dfs(0)
        return res

if __name__ == "__main__":
    h = Solution()
    n = 2
    result = h.printNumbers(n)
    print(result)