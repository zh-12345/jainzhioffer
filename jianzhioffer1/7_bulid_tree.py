# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def ConstructCore(startpreorder, endpreorder, startinorder, endinorder):
            rootvalue = preorder[startpreorder]
            root = TreeNode(rootvalue)
            privot = maps[preorder[startpreorder]]
            if privot-startinorder>0:
                root.left = ConstructCore(startpreorder + 1, startpreorder + privot - startinorder, startinorder,
                                          privot - 1)
            if privot-startinorder<endpreorder-startpreorder:
                root.right = ConstructCore(startpreorder + privot - startinorder + 1, endpreorder, privot + 1, endinorder)
            return root

        if len(preorder) < 0 or len(inorder) < 0:
            return None
        maps = {num: index for index, num in enumerate(inorder)}
        return ConstructCore(0, len(preorder) - 1, 0, len(inorder) - 1)

if __name__=='__main__':
    h = Solution()
    preorder= [3,9,20,15,7]
    inorder=[9,3,15,20,7]
    result =h.buildTree(preorder,inorder)