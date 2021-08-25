class Solution():
    def longestOnes(self, nums, k):
        n = len(nums)
        ans = 0
        sum = [0] *(n+1)

        def check(sum, l, r, k):
            tol = sum[r + 1] - sum[l]
            len = r - l + 1
            return len - tol <= k

        for i in range(1,n + 1):
            sum[i] = sum[i - 1] + nums[i - 1]
        for j in range(0,n):
            l = 0
            r = j
            while l < r:
                mid = (l + r) // 2
                if check(sum, mid, j, k):
                    r = mid
                else:
                    l = mid + 1

            if check(sum, r, j, k):
                ans = max(ans, j - r + 1);

        return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    h = Solution()
    result = h.longestOnes(nums, k)
    print(result)
