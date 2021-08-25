def quick_sort(alist, first, last):
    #     先确定第一个值为中间值
    if first >= last:
        return
    mid_value = alist[first]
    # n = len(alist)
    low = first
    high = last
    # 递归思想传的始终是原有列表

    # 首先判断high 当前指的元素与中间值的大小
    while low < high:
        # low  high 交替执行
        # 相等状态 放在一遍，要么在左边，要么在右边

        while low < high and alist[high] >= mid_value:
            high -= 1
        # if low < high:
        alist[low] = alist[high]
        # 一旦low 下标对应的值和high发生交换

        # low移动开始，开始判断low  当前指的元素与中间值的大小
        while low < high and alist[low] < mid_value:
            low += 1
        # 退出循环，找到一个比基准元素大的，然后high对应的值发生变化，
        # if low < high:
        alist[high] = alist[low]
    alist[low] = mid_value
    quick_sort(alist, first, low - 1)
    quick_sort(alist, low + 1, last)


if __name__ == "__main__":
    li = [23, 2, 56, 7, 2, 4, 5, 7, 889, 432, 234]
    # li = [54,26,93,17,77,31,44,55,20,77,78]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
