class Solution():
    def findRepeatNum(self,nums):
        dic={}
        for num in nums:
            if num in dic:
                return num
            dic.setdefault(num,0)
        return -1

    def findRepeatNum2(self, nums):
        i =0
        while i<len(nums):
            while nums[i] == i:
                i += 1
            if nums[i] ==nums[nums[i]]:
                return nums[i]
            temp = nums[i]
            nums[i] =nums[temp]
            nums[temp] =temp

        return -1

if __name__ =="__main__":
    h = Solution()
    # nums =[2,3,1,0,2,5,3]
    nums = [2,3,5,4,3,2,6,7]
    result=h.findRepeatNum(nums)
    print(result)
    print(nums)