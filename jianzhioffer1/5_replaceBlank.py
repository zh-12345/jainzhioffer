class Solution:
    def replaceSpace(self, s: str) -> str:

        length1 = len(s)
        if length1 <= 0:
            return s
        s = list(s)
        count = 0
        for i in range(length1):
            if s[i] == ' ':
                count += 1
        length = length1 + 2 * count
        s = s+['']*2 * count
        p1 = length1 - 1
        p2 = length - 1
        while p1>=0 and p1<p2:
            if s[p1] == ' ':
                s[p2] ='0'
                p2 -= 1
                s[p2] ='2'
                p2 -=1
                s[p2]='%'
                p2-=1
            else:
                s[p2]=s[p1]
                p2 -=1
            p1 -=1

        return "".join(s)

    def replaceSpace2(self, s: str) -> str:

        res = []
        for c in s:
            if c == ' ':
                res.append('%20')
            else:
                res.append(c)
        return "".join(res)

if __name__ == '__main__':
    h = Solution()
    s = '     '
    result = h.replaceSpace2(s)
    print(result)
