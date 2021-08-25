class Solution():
    def isIsomorphic(self,str,t):

        if s.strip()=='' or t.strip()=='':
            return False
        dict1 = {}
        dict2 ={}
        for i in range(len(str)):
            if (str[i] in dict1 and dict1[str[i]] != t[i]) or t[i] in dict2 and dict2[t[i]] != str[i]:
                return False
            dict1[str[i]] = t[i]
            dict2[t[i]] = str[i]
        return True

if __name__ =='__main__':
    h = Solution()
    s= 'foo'
    t= 'bar'
    print(h.isIsomorphic(s,t))