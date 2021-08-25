def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    # gap = 4
    # gap变化到1之前，可以取1
    while gap > 0:
        #     希尔排序和插入算法的区别就是 gap 步长
        for i in range(gap, len(alist)):
            # i 取的是gap gap+1 gap +2 , n-1
            j = i
            while j > 0:
                if alist[j] < alist[j - gap]:
                    alist[j], alist[j - gap] = alist[j - gap], alist[j]
                    j -= gap
                else:
                    break
        gap //= 2


if __name__ == "__main__":
    li = [23, 2, 56, 7, 2, 4, 5, 7, 889, 432, 234]
    print(li)
    shell_sort(li)
    print(li)
