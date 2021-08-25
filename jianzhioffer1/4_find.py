from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:

        found = False
        rows = len(matrix)
        if rows <= 0:
            return found
        columns = len(matrix[0])
        if rows > 0 and columns > 0:
            row = 0
            column = columns - 1
            while row < rows and column >= 0:
                if matrix[row][column] == target:
                    found = True
                    break
                elif matrix[row][column] > target:
                    column -= 1
                else:
                    row += 1
        return found

if __name__=='__main__':
    h =Solution()
    imtx=[]
    for i in range(4):
        row =map(int,input().split())
        imtx.append(list(row))
    result = h.findNumberIn2DArray(imtx,7)
    print(result)