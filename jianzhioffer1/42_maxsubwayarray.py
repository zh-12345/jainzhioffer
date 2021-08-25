class Solution():
    def maxSubarray(self,nums):
        if len(nums) <= 0:
            return 0
        if len(nums) ==1:
            return nums[0]
        nCursum =-2**31-1
        res =-2**31-1
        for i in range(len(nums)):
            if nCursum + nums[i] <= nums[i]:
                nCursum = nums[i]
            else:
                nCursum += nums[i]
            res = max(res,nCursum)
        return res

    def maxSubarray2(self, nums):
        # dp[i] 代表 i 之前的所有元素的连续子数组最大和
        n = len(nums)
        dp = [0] * (n + 1)
        ans = nums[0]
        for i in range(1, n + 1):
            dp[i] = max(nums[i - 1], dp[i - 1] + nums[i - 1])
            ans = max(ans, dp[i])

        return ans


if __name__=='__main__':
    h =Solution()
    nums =[-2,5,3,-6,8,9]
    result = h.maxSubarray2(nums)
    print(result)
