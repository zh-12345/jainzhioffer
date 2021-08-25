import collections
class Solution():
    def FirstNotReaptingChar(self,s):
        length = len(s)
        if length <= 0:
            return ' '
        dict ={}
        i = 0
        while i < length:
            ch =s[i]
            dict.setdefault(ch,0)
            dict[ch] +=1
            i += 1
        for i in range(length):
            if s[i] in dict:
                if dict[s[i]] ==1:
                    return s[i]
        return ' '

    def First2(self,s):
        frequency = collections.Counter(s)
        for i,ch in enumerate(s):
            if frequency[ch] == 1:
                return ch
        return ' '

if __name__=='__main__':
    h =Solution()
    s='cc'
    # result = h.FirstNotReaptingChar(s)
    result = h.First2(s)
    print(result)
