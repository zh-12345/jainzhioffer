class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x ==0:
            return 0
        if n ==0:
            return 1
        flag = False
        if n <0:
            flag = True
            n = -n
        res =1
        while n :
            if n & 1:
                res *= x
            x *= x
            n = n>>1
        return res if not flag else 1/res
if __name__=='__main__':
    h =Solution()
    x = -2.00000
    n = -2
    result = h.myPow(x,n)
    print(result)