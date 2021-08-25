class Solution():
    def missingNumber(self,nums):
       nums.sort()
       left =0
       right= len(nums)
       while right > left:
           mid = (right + left)//2
           if nums[mid] > mid:
               right = mid
           else:
               left = mid +1
       return right
    def missingNumber2(self,nums):
         missing = len(nums)
         for i,num in enumerate(nums):
              missing ^= i^num
         return missing

    def missingNumber3(self,nums):
        num_set = set(nums)
        n = len(nums) +1
        for number in range(n):
            if number not in num_set:
                return number

if __name__ =='__main__':
    h = Solution()
    nums =[0,1]
    result = h.missingNumber3(nums)
    print(result)