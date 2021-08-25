# 顺序表比较大小是交换数据，如果是链表，交换节点
def bubble_sort(alist):
    # 如果直接用list本身操作，那就是元素本身，不好直接交换
    # 一共有N个元素就比较N-1次，
    n = len(alist)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]


def bubble_sort1(alist):
    # 如果直接用list本身操作，那就是元素本身，不好直接交换
    # 一共有N个元素就比较N-1次，
    n = len(alist)
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]


def bubble_sort2(alist):
    # 如果直接用list本身操作，那就是元素本身，不好直接交换
    # 一共有N个元素就比较N-1次，
    n = len(alist)
    for i in range(n-1):
        count = 0
        for j in range(0, n-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                count += 1
        if count == 0:
            return


if __name__ == "__main__":
    li = [23, 2, 56, 7, 2, 4, 5, 7, 889, 432, 234]
    print(li)
    bubble_sort1(li)
    print(li)
    # 这两种写法是一致的
    # a = [i for i in range(5)]
    # b = [i for i in range(0, 5)]