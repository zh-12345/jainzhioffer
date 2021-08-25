def select_sort(alist):
    for i in range(len(alist)-1):
        mini = i
        # j = i+1
        for j in range(i+1,len(alist)):
            # 先行找到最小值的小标，
            if alist[mini] > alist[j]:
                mini = j
        alist[i], alist[mini] = alist[mini], alist[i]


if __name__ == "__main__":
    li = [23, 2, 56, 7, 2, 4, 5, 7, 889, 432, 234]
    print(li)
    select_sort(li)
    print(li)