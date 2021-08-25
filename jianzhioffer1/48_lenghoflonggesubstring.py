class Solution:
    def lengthoflongsubstring(self, s):
        left = 0
        right = 0
        window = {}
        res = 0
        # for ss in s:
        while right < len(s):
            c1 = s[right]
            window.setdefault(c1, 0)
            window[c1] += 1
            right += 1
            while window[c1] > 1:
                c2 = s[left]
                window[c2] -= 1
                left += 1
            res = max(res, right - left)
        return res

    def lengthoflongsubstring2(self, s):
        sub = ""
        largest = 0

        # 循环字符串，将当前字符加入子字符串，并检查长度
        for i in range(len(s)):
            if s[i] not in sub:
                # 当前字符不存在于子字符串中，加入当前字符
                sub += s[i]
            else:
                # 如果当前子字符串的长度超过了之前的记录
                if len(sub) > largest:
                    largest = len(sub)
                # 将子字符串从当前字符处+1切片至最后，并加入当前字符
                sub = sub[sub.find(s[i]) + 1:] + s[i]

        # 如果最后的子字符串长度超过了之前的记录
        if len(sub) > largest:
            return len(sub)
        return largest

    def lengthoflongsubstring3(self, s):
        dic = {}
        left = -1
        res = 0

        for i in range(len(s)):
            if s[i] in dic:
                left = max(left, dic.get(s[i]))  # 更新左指针
            dic[s[i]] = i
            res = max(res, i - left)
        return res

    def lenghoflongsubstring4(self, s):
        dic = {}
        res = temp = 0
        # temp=0
        for j in range(len(s)):
            i = dic.get(s[j], -1)
            dic[s[j]] = j
            temp = temp + 1 if temp < j - i else j - i
            res = max(res, temp)
        return res


if __name__ == "__main__":
    h = Solution()
    s = 'pwwkew'
    s1 = "aabaab!bb"
    result = h.lenghoflongsubstring4('aaaaaaa')
    print(result)
