class Solution():
    def maximumProduct(self,nums):
        if len(nums)<0:
            return None
        m= len(nums)
        nums.sort()
        maximum = nums[0]*nums[1] * nums[m-1]
        return max(maximum, nums[m-1]*nums[m-2]*nums[m-3])
if __name__=='__main__':
    h = Solution()
    nums =[-1,2,3,4]
    result = h.maximumProduct(nums)
    print(result)