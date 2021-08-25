class Solution():
    def reverse(self,x):
        if -10<x<10:
            return x
        str_x= str(x)
        if str_x[0] == '+' or str_x[0] =='-':
            str_x = str_x[:0:-1]
            x= int(str_x)
            x= -x
        else:
            str_x= str_x[::-1]
            x = int(str_x)
        return x if -2**31-1 <x<2**31-1  else 0


if __name__=="__main__":
    h = Solution()
    x= -123
    result= h.reverse(x)
    print(result)