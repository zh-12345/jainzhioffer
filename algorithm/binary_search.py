def binary_search(alist, item):
    # 递归的思想
    n = len(alist)

    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid + 1:], item)
    return False


def binary_search_2(alist,item):
    n = len(alist)
#     非递归版本，只能在原有列表中操作，所以需要知道列表的起始和终止位置,改变起始和终止位置，就能决定搜索范围
    first = 0
    last = n-1
    # 需要一个循环条件判断，什么时候代表没有找到,first和last的值一直都在改变，一旦满足什么条件的时候，就不用再寻找了
    while first <= last:
        mid = (first + last)//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


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
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
    print(binary_search(li,889))
    print(binary_search(li, 100))
    print(binary_search_2(li, 889))
    print(binary_search_2(li, 100))
