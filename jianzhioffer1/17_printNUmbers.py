from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = []
        if n <= 0:
            return res
        number = ['0' for i in range(n)]

        def Increment(number):
            isOverflow = False
            nTakeOver = 0
            nLength = len(number)
            for i in range(nLength - 1, -1, -1):
                nsum = ord(number[i]) - ord('0') + nTakeOver
                if i == nLength - 1:
                    nsum += 1
                if nsum >= 10:
                    if i == 0:
                        isOverflow = True
                    else:
                        nsum -= 10
                        nTakeOver = 1
                        number[i] = str(nsum)
                else:
                    number[i] = str(nsum)
                    break
            return isOverflow

        def PrintNumber(number):
            ss = ''
            isBeginning0 = True
            nLength = len(number)
            s = ''.join(number)
            for i in range(nLength):
                if isBeginning0 and number[i] != '0':
                    isBeginning0 = False
                if not isBeginning0:
                    ss += s[i]

            return ss

        while not Increment(number):
            ss = PrintNumber(number)
            res.append(int(ss))
            # res = list(map(int, res))
        return res


if __name__ == "__main__":
    h = Solution()
    n = 5
    result = h.printNumbers(n)
    print(result)
