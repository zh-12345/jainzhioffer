class Solution():
    def addbignum(self,a,b):
        def PrintNumber(number):
            ss = ''
            isBeginning0 = True
            nLength = len(number)
            s = ''.join(number)
            for i in range(nLength):
                if isBeginning0 and number[i] != '0':
                    isBeginning0 = False
                if not isBeginning0:
                    ss += s[i]

            return ss
        flag = True
        i=0
        if len(a)>len(b):
            length= len(a)-len(b)
            b='{}{}'.format('0'*length,b)
        elif len(a) <len(b):
            length=len(b)-len(a)
            a='{}{}'.format('0'*length,a)
            flag= False
            a,b=b,a
        else:
            while(i<len(a)):
                if ord(a[i])-ord('0')< ord(b[i])-ord('0'):
                    flag= False
                    a,b=b,a
                    break
                i +=1


        sum_list = ['0' for i in range(len(a))]
        nTakeOver =0
        for i in range(len(a)-1,-1,-1):
            nsum = ord(a[i])-ord('0')-(ord(b[i])-ord('0'))-nTakeOver
            if nsum<0:
                nsum +=10
                nTakeOver =1
                sum_list[i]=str(nsum)
            else:
                sum_list[i]=str(nsum)
                nTakeOver =0
        sum_list1=PrintNumber(sum_list)
        return sum_list1 if flag else '{}{}'.format('-',sum_list1)

if __name__ == "__main__":
    h = Solution()
    n = '6456456754967595476'
    m ='312321321321321356577869973523323757753625424324324234'
    result = h.addbignum(n,m)
    print(result)
