class Solution():
    def MaxDiff(self,prices):
        if len(prices) < 2:
            return 0
        dp_i_0 =0
        dp_i_1 = -2**31-1
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0,dp_i_1+ prices[i])
            dp_i_1 = max(dp_i_1,-prices[i])
        return dp_i_0
if __name__=='__main__':
    h = Solution()
    prices=[9,11,8,5,7,12,16,14]
    result=h.MaxDiff(prices)
    print(result)