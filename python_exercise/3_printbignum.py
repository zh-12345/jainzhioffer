class Solution():
    def sub(self,a,b):
        # a,b = line.strip().split()
        a = [int(item) for item in a]
        b = [int(item) for item in b]
        res = ''
        for i in range(len(b)):
            flag_a = len(a)-1-i
            flag_b = len(b)-1-i
            if a[flag_a]>= b[flag_b]:
                res = str(a[flag_a]-b[flag_b])+res
            else:
                res = str(10+a[flag_a]-b[flag_b])+res
                while a[flag_a-1]==0:
                    a[flag_a-1]=9
                    flag_a -= 1
                a[flag_a-1] -= 1
        for j in range(len(a)-1-i-1,-1,-1):
            res = str(a[j])+res
        zero_flag=0
        for i in range(len(res)):
            if res[i]!='0':
                zero_flag=1
                break
        if zero_flag==0:
            return 0
        return res[i:]
if __name__ == "__main__":
    h = Solution()
    n = '20'
    m ='18'
    result = h.sub(n,m)
    print(result)