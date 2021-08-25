class Solution():
    def FindUnsortedSubarray(self,nums):
        if len(nums) <0:
            return -1
        nums2 = list(nums)
        nums.sort()
        left,right = 0,-1
        for i in range(0,len(nums)):
            if nums2[i] != nums[i]:
                left = i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums2[i] != nums[i]:
                right = i
                break
        return right-left +1

    def FindUnsortedSubarray2(self, nums):
        if len(nums)<0:
            return -1
        stack = list()
        left = len(nums)
        right = 0
        for i in range(0,len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                left= min(left,stack.pop())
            stack.append(i)
        stack.clear()
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] <nums[i]:
                right = max(right,stack.pop())
            stack.append(i)
        if right >left:
            return right-left +1
        else:
            return 0


if __name__=='__main__':
    h = Solution()
    # nums = [2,6,4,8,10,9,15]
    nums =[1,2,3,4]
    result = h.FindUnsortedSubarray2(nums)
    print(result)

