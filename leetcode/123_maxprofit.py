class Solution():
    def maxProfi(self, prices):
        dp_i_1_0 = 0
        dp_i_1_1 = -2 ** 32 - 1
        dp_i_2_0 = 0
        dp_i_2_1 = -2 ** 32 - 1
        for i in range(len(prices)):
           dp_i_2_0 = max(dp_i_2_0, dp_i_2_1 + prices[i])
           dp_i_2_1 = max(dp_i_2_1, dp_i_1_0 - prices[i])
           dp_i_1_0 = max(dp_i_1_0,dp_i_1_1+ prices[i])
           dp_i_1_1 = max(dp_i_1_1, - prices[i])



        return dp_i_2_0


if __name__ == '__main__':
    h = Solution()
    nums = [3,3,5,0,0,3,1,4]
    result = h.maxProfi(nums)
    print(result)