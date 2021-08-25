import numpy as np


class Solution:
    def print_array(self, numbers, row, column):
        if bool(1 - (numbers.any())) or row <= 0 or column <= 0:
            return numbers
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        result = []
        visited = [['$'] * column for i in range(row)]
        m = column - 1
        n = row - 1
        x, y = 0, 0
        temp = 0
        while len(result) < row * column:
            result.append(numbers[x][y])
            visited[x][y] = '#'
            nx, ny = direction[temp][0] + x, direction[temp][1] + y
            if nx > n or ny > m or visited[nx][ny] == '#' or nx < 0 or ny < 0:
                temp += 1
                temp = temp % 4
                nx, ny = direction[temp][0] + x, direction[temp][1] + y
            x, y = nx, ny
        return result

    def print_array2(self, numbers):
        row = len(numbers)
        column = len(numbers[0])
        if bool(1 - (numbers.any())) or row <= 0 or column <= 0:
            return numbers
        start = 0
        res = []

        def printMatrixInCircle(numbers, row, column, start):
            endColumn = column - 1 - start
            endRow = row - 1 - start
            for i in range(start, endColumn+1):
                res.append(numbers[start][i])
            if start < endRow:
                for i in range(start+1, endRow+1):
                    res.append(numbers[i][endColumn])
            if start < endRow and start < endColumn:
                for i in range(endColumn-1, start - 1, -1):
                    res.append(numbers[endRow][i])
            if start < endRow -1 and start < endColumn:
                for i in range(endRow-1, start, -1):
                    res.append(numbers[i][start])

        while start < min(row, column) / 2:
            printMatrixInCircle(numbers, row, column, start)
            start += 1
        return res

if __name__ == "__main__":
    h = Solution()
    numbers = np.array(range(1, 17)).reshape(4, 4)
    print(numbers)
    # visited = [[0] * 4 for i in range(3)]
    # visited = [0]*3
    # print(visited)
    # print(numbers.any())
    # print(bool(1-(numbers.any())))
    # h.print_array(numbers,4,4)
    resultarray = h.print_array2(numbers)
    print(resultarray)
