class Solution():
    def maxProfi(self,prices):
        dp_i_0 = 0
        dp_i_1 = -2**32-1
        dp_pre_0 = 0
        for i in range(len(prices)):

            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = dp_i_0
            dp_i_0 = max(dp_i_0,dp_i_1 + prices[i])




        return dp_i_0
if __name__ == '__main__':
    h =Solution()
    nums=[1,2,3,0,2]
    result = h.maxProfi(nums)
    print(result)