class Solution:
    def twoSum(self,nums, target):
        hashTable={}
        # 寻找两个目标数值
        for i, n in enumerate(nums):
            other_num = target - n
            # 如果存在这个余数 other_num
            if other_num in hashTable.keys():
                # 查看是否存在哈希表里，如果存在的话就返回数组
                return [hashTable[other_num],i ]
            # 如果不存在的话继续处理剩余的数
            hashTable[n] = i

if __name__ == "__main__":
    h = Solution()
    nums =[3,1,3,6]
    target = 6
    result = h.twoSum(nums,target)
    print(result)