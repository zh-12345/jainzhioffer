class Solution:
    def reverse_string1(self, s):
        r = s[::-1]
        return r

    def reverse_string2(self, s):
        r = list(s)
        result1 = ''
        while len(r) > 0:
            result1 += r.pop()
        return result1

    def reverse_string3(self, s):
        r = list(s)
        r.reverse()
        print("".join(r))

    def reverse_string4(self, s):
        if s is None or s.isspace() is True:
            return s
        s = list(s)
        length = len(s)
        i, j = 0, length - 1
        while i < j:
            if i == j:
                break
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        s = "".join(s)
        return s

    def reverse_sentence(self, pData):
        if pData is None or pData.isspace() is True:
            return None
        # result = self.reverse_string4(pData)
        # return result
        pData = pData.strip()
        i = j = len(pData) - 1
        res = []
        while i >= 0:
            while i >= 0 and pData[i] != ' ':
                i -= 1
            res.append(pData[i + 1:j + 1])
            while pData[i] == ' ':
                i -= 1
            j = i

        return " ".join(res)

    #    这个思路其实并没有用到之前反转的思想，首先就是去除掉首尾空格，
    # 然后倒序遍历，查找，从最后一个字符往前找，直到为空，就找到了首尾位置，然后将其剪切到列表当中
    # 然后再跳过这个空格，将头部的位置传给尾部的位置，循环这个过程，直到遍历到尾部结束。

    def reverse_sentence1(self, pData):
        if pData.isspace() is True:
            return None
        if pData.strip() == '':
            return None
        result = self.reverse_string4(pData)
        # return result
        # pData = pData.strip()
        #     result= result+'\0'
        i = j = 0
        res = ''
        while i <= len(result) - 1:
            while i <= len(result) - 1 and result[i] != ' ':
                i += 1
            if i > len(result) - 1:
                res += self.reverse_string4(result[j:])
            else:
                res += self.reverse_string4(result[j:i]) + ' '
                while result[i] == ' ':
                    i += 1
                j = i
        return res

    def left_reverse_vocalbulary(self,pData,m):
        if pData.isspace() is True:
            return None
        if pData.strip() == '':
            return None
        if m > len(pData):
            return False
        res=' '
        res += self.reverse_string4(pData[:m])
        res += self.reverse_string4(pData[m:])
        res = self.reverse_string4(res)
        return res


if __name__ == "__main__":
    h = Solution()
    result = []
    # ss = 'shdjeifirh'
    # result =h.reverse_string1(ss)
    # print(result)
    # test02
    # result = h.reverse_string2(ss)
    # print(result)
    # test03
    # result=h.reverse_string4(ss)
    # print(result)
    sss = 'abcdefg'
    #   test04
    # result1 = h.reverse_sentence(sss)
    # result1 = h.reverse_sentence1(sss)
    result1 = h.left_reverse_vocalbulary(sss,8)
    print(result1)
