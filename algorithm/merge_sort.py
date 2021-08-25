def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2
    # left采用归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid])
    # right 采用归并排序后形成的有序的新的列表
    right_li = merge_sort(alist[mid:])

#     将两个有序的子序列合并成一个新的整体
#      merge(right,left)
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
#     退出循环的时候，就是有一边的序列已经为空，则将剩余的序列复制过来
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == "__main__":
    li = [23, 2, 56, 7, 2, 4, 5, 7, 889, 432, 234]
    print(li)

    print(merge_sort(li))