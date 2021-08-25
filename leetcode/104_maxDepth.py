import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 树其实相当于对列表的一个扩充
import collections


class Node(object):
    def __init__(self, item):
        self.item = item
        # 不同于链表的是，连接区域不同，二叉树有左右两个子树的连接区域
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        # 不考虑头插和任意位置插，往完全二叉树努力，在最后位置插入新增加的数据
        # 广度优先遍历，层次优先遍历，
        node = Node(item)
        if self.root is None:
            self.root = node
            return

        # 使用队列来解决问题,队列不为空
        queue = [self.root]
        while queue:
            # 首先取出这个节点
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def breadth_travel(self):
        # 广度遍历，一层一层的搜索

        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=" ")
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

    def preorder(self, node):
        # 递归实现先序遍历,把每断个子树都当做一棵树来判，这个时候的根节点是在变化的
        # 这个也就是递归的终止条件
        if node is None:
            return
        print(node.item, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def ineorder(self, node):
        # 递归实现中序遍历,把每个子树都当做一棵树来判断，
        # 都是一棵树，然后打印的都是根节点
        # 这个时候的根节点是在变化的
        # 这个也就是递归的终止条件
        if node is None:
            return
        self.ineorder(node.left)
        print(node.item, end=" ")
        self.ineorder(node.right)

    def postorder(self, node):
        # 递归实现后序遍历,把每个子树都当做一棵树来判断，
        # 都是一棵树，然后打印的都是根节点
        # 这个时候的根节点是在变化的
        # 这个也就是递归的终止条件
        if node is None:
            return
        self.postorder(node.left)

        self.postorder(node.right)
        print(node.item, end=" ")

    def maxDepth(self, root):
        if not root:
            return 0
        nleft = self.maxDepth(root.left)
        nright = self.maxDepth(root.right)
        return nleft + 1 if nleft > nright else nright + 1

    def maxDepth2(self, root):

        if not root:
            return 0
        queue = collections.deque([root])
        depth = 0
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.ineorder(tree.root)
    print(" ")
    tree.postorder(tree.root)
    print(" ")
    result = tree.maxDepth2(tree.root)
    print(result)

# 学习一下广度优先搜索
#
