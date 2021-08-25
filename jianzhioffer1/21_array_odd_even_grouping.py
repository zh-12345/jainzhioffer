class Solution:
    def array_odd_even_grouping(self, li):
        if len(li) == 0:
            return None
        left = 0
        right = len(li) - 1
        while left < right:
            while left < right and li[left] % 2 == 1:
                left += 1
            li[right],li[left] = li[left],li[right]
            while left < right and li[right] % 2 == 0:
                right -= 1
            li[left],li[right] = li[right],li[left]
        return li

    def array_odd_even_grouping2(self, li):
        if len(li) == 0:
            return None
        def isEven(n):
            if n % 2 == 1:
                return True
            else:
                return False
        left = 0
        right = len(li) - 1
        while left < right:
            while left < right and isEven(li[left]):
                left += 1
            li[right], li[left] = li[left], li[right]
            while left < right and bool(1-(isEven(li[right]))):
                right -= 1
            li[left], li[right] = li[right], li[left]
        return li

    def array_odd_even_grouping3(self, li):
        if len(li) == 0:
            return None
        slow = fast = 0
        while fast < len(li):
            if li[fast] % 2 == 1:
                li[fast],li[slow] = li[slow],li[fast]
                slow += 1
            fast += 1
        return li



if __name__ == "__main__":
    h = Solution()
    nums = [1, 2, 3, 4]
    # nums = [22,3]
    result = h.array_odd_even_grouping3(nums)
    print(result)
