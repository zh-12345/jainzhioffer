import sys
class Solution():
    g_nStatus = 0
    # 若非法输入，则这个值设置为1,初始值为1
    def strToInt(self,s):
        g_nStatus=0
        s = s.strip()
        if s =='':
            g_nStatus=1
            return 0
        sign =1
        num  =0
        ss =s[:]
        bndry = (2**31-1)//10
        if s[0]== '+':
            sign =1
            ss = s[1:]
        elif s[0] =='-':
            sign =-1
            ss = s[1:]
        for sss in ss:
            if sss >= '0' and sss <= '9':

                if num > bndry or num == bndry and sss>'7':
                    return 2**31-1 if sign == 1 else -2**31-1
                num = num * 10 + ord(sss) - ord('0')
            else :
                g_nStatus = 1
                break
        return num*sign

if __name__ =='__main__':
    h = Solution()
    nums ='2147483646'
    result = h.strToInt(nums)
    print(result)