import collections


class Solution:
    def quick_sort(self, li, first, last):
        if first >= last:
            return
        mid_value = li[first]
        low = first
        high = last
        while low < high:
            while low < high and li[high] >= mid_value:
                high -= 1
            li[low] = li[high]
            while low < high and li[low] < mid_value:
                low += 1
            li[high] = li[low]
        li[low] = mid_value
        self.quick_sort(li, first, low - 1)
        self.quick_sort(li, low + 1, last)

    def majority_element1(self, li):
        if len(li) == 0:
            return False
        self.quick_sort(li, 0, len(li) - 1)
        result = li[len(li) // 2]

        def CheckMoreThanHalf(numbers, len, number):
            times = 0
            for i in range(len):
                if numbers[i] == number:
                    times += 1
            isMoreThanHalf = False
            if times * 2 > len:
                isMoreThanHalf = True
            return isMoreThanHalf

        if CheckMoreThanHalf(li, len(li), result):
            result = 0
        return result

    def majority_element2(self, li):
        if len(li) == 0:
            return False
        dic = collections.Counter(li)
        for key,value in dic.items():
            if value > len(li) //2:
                return key

    def majority_element3(self, li):
        if len(li) == 0:
            return False
        times = 0
        for num in li:
            if times == 0:
                result = num
                times =1
            elif num == result:
                times += 1
            else:
                times -= 1
        def CheckMoreThanHalf(numbers, len, number):
            times = 0
            for i in range(len):
                if numbers[i] == number:
                    times += 1
            isMoreThanHalf = False
            if times * 2 > len:
                isMoreThanHalf = True
            return isMoreThanHalf

        if CheckMoreThanHalf(li, len(li), result):
            return result
        else:
            return 0


if __name__ == "__main__":
    h = Solution()
    alist = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    # h.quick_sort(alist, 0, len(alist) - 1)
    # print(alist)
    result = h.majority_element3(alist)
    print(result)
