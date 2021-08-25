# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack_1 = [root]
        stack_2 = []
        current = False

        while stack_1 or stack_2:
            temp = []
            if not current:
                for i in range(len(stack_1)):
                    node = stack_1.pop()
                    temp.append(node.val)
                    if node.left:
                        stack_1.append(node.left)
                    if node.right:
                        stack_1.append(node.right)
                    current = True
            else:
                for i in range(len(stack_2)):
                    node = stack_2.pop()
                    temp.append(node.val)
                    if node.right:
                        stack_2.append(node.left)
                    if node.right:
                        stack_2.append(node.right)
                    current = False
            res.append(temp)
        return res
if __name__=='__main__':
    h


