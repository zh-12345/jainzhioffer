class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# 二叉树的广度优先遍历
def bfs(root):
    result = []
    if root == None:
        return result
    queue = [root]
    while len(queue) > 0:
        head = queue[0]     # 获取队首元素
        queue.remove(head)  # 队首元素出队列
        result.append(head)
        if head.left != None:
            queue.append(head.left) # 左子节点入队
        if head.right != None:      # 右子节点入队
            queue.append(head.right)
    return result


if __name__ == "__main__":
    # 先构建二叉树
    node7 = Node('G', None, None)
    node5 = Node('E', node7, None)
    node4 = Node('D', None, None)
    node2 = Node('B', node4, node5)
    node6 = Node('F', None, None)
    node3 = Node('C', None, node6)
    node1 = Node('A', node2, node3)

    result = bfs(node1)			# 广搜
    print([x.val for x in result])
