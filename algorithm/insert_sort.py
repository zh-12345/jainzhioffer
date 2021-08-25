def insert_sort(alist):
    for i in range(1, len(alist)):
        # i最后取的值是【1,2，...n-1]
        j = i
        while j > 0:
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
                j -= 1
            else:
                break


if __name__ == "__main__":
    li = [23, 2, 56, 7, 2, 4, 5, 7, 889, 432, 234]
    print(li)
    insert_sort(li)
    print(li)