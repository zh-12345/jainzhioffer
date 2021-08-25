class Solution:
    def isNumeric(self,s):
        if s.strip == '':
            return False
        s = s.strip()
        n = len(s)
        index = 0
        has_num = has_e = has_sign = has_dot = False
        # 处理开头的空格，index相应的后移
        # 如果当前字符是数字，将索引移动到非数字或遍历到末尾位置
        while index < n and s[index] == ' ':
            index += 1
        while index < n:
            while index < n and '0' <= s[index] <= '9':
                index += 1
                has_num = True
            if index == n:
                break
            if s[index] == 'e' or s[index] == 'E':
                if has_e or not has_num:
                    return False
                has_e = True
                has_num = has_sign = has_dot = False
            elif s[index] == '+' or s[index] == '-':
                if has_sign or has_num or has_dot:
                    return False
                has_sign = True
            elif s[index] == '.':
                if has_dot or has_e:
                    return False
                has_dot = True
            elif s[index] == ' ':
                break
            else:
                return False
            index += 1
        while index < n and s[index] == ' ':
            index += 1
        return has_num and index == n

#
# 然后进入循环，遍历字符串
#
#     如果当前字符c是数字：将hasNum置为true，index往后移动一直到非数字或遍历到末尾位置；如果已遍历到末尾(index == n)，结束循环
#     如果当前字符c是'e'或'E'：如果e已经出现或者当前e之前没有出现过数字，返回fasle；否则令hasE = true，并且将其他3个flag全部置为false，因为要开始遍历e后面的新数字了
#     如果当前字符c是+或-：如果已经出现过+或-或者已经出现过数字或者已经出现过'.'，返回flase；否则令hasSign = true
#     如果当前字符c是'.'：如果已经出现过'.'或者已经出现过'e'或'E'，返回false；否则令hasDot = true
#     如果当前字符c是' '：结束循环，因为可能是末尾的空格了，但也有可能是字符串中间的空格，在循环外继续处理
#     如果当前字符c是除了上面5种情况以外的其他字符，直接返回false
#
# 处理空格，index相应的后移
# 如果当前索引index与字符串长度相等，说明遍历到了末尾，但是还要满足hasNum为true才可以最终返回true，因为如果字符串里全是符号没有数字的话是不行的，而且e后面没有数字也是不行的，但是没有符号是可以的，所以4个flag里只要判断一下hasNum就行；所以最后返回的是hasNum && index == n
# 如果字符串中间有空格，按以上思路是无法遍历到末尾的，index不会与n相等，返回的就是false


if __name__ == '__main__':
    h =Solution()
    numeric = 'e9'
    # numeric = '2e0'
    result =h.isNumeric(numeric)
    print(result)