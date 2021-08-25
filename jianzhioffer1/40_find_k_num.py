class Solution:
    def daycost(self , len , m , n ):
        if n >= m and len > m:  # 需注意处理len<=m时的特殊情况
            return -1
        c = 0
        while len > 0:
            c += 1
            len -= m
            if len <= 0:
                return c
            len += n
        return -1
if __name__=="__main__":
    h = Solution()
    result = h.daycost(10,4,3)
    print(result)