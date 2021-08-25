from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        if rows<1 or cols <1 or not word:
            return False
        multilist = [[False for col in range(cols)] for row in range(rows)]
        pathLength = 0
        def hasPathCore(board,row,col,word,pathLength):
            if pathLength == len(word):
                return True
            hasPath = False
            if row>=rows or col >= cols or row <0 or col<0 or board[row][col] != word[pathLength] or multilist    [row][col]:
                return False
            multilist[row][col]=True
            dx=[0,1,0,-1]
            dy=[1,0,-1,0]
            for i in range(4):
                x = row +dx[i]
                y = col +dy[i]
                if hasPathCore(board,x,y,word,pathLength+1):
                     return True
            multilist[row][col]= False
            return hasPath
        for row in range(rows):
            for col in range(cols):
                if hasPathCore(board,row,col,word,pathLength):
                    return True
        return False
if __name__=='__main__':
    h =Solution()
    board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word="ABCCED"
    result = h.exist(board,word)
    print(result)