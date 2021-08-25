class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        # if not root.left and not root.right:
        #     return
        temp = root.left
        root.left = root.right
        root.right = temp

        self.mirrorTree(root.left)

        self.mirrorTree(root.right)
        return root