# This is a sample Python script.
from typing import List
import unittest

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# 剑指第一题。
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return num
            hashmap[num] = 1


    def findRepeatNumber2(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i]!=i:
                # a=nums[i]
                # b=nums[nums[i]]
                if nums[i]==nums[nums[i]]:
                    return nums[i]
                nums[nums[i]],nums[i]=nums[i],nums[nums[i]]


# 简单定义一个对象
test= Solution()
# a=[2, 3, 1, 0, 2, 5, 3]
a=[0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
result=test.findRepeatNumber(a)
print(result)
