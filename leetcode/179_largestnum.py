import functools
class Solution():
    def largetsnum(self,nums):
        if not len(nums):
            return nums
        nums_str = list(map(str,nums))
        compare = lambda x,y: 1 if x+y < y+x else -1
        nums_str.sort(key = functools.cmp_to_key(compare))
        res=''.join(nums_str)
        if res[0] =='0':
            res ='0'
        return res

    def largestnum1(self,nums):
        if not len(nums):
            return nums
        nums_str =list(map(str,nums))
        for i in range(len(nums_str)-1):
            for j in range(i+1,len(nums_str)):
                if nums_str[i]+nums_str[j] < nums_str[j]+nums_str[i]:
                    nums_str[i],nums_str[j] = nums_str[j],nums_str[i]
        res = ''.join(nums_str)
        if res[0] == '0':
            res = '0'
        return res

    def lagerstnum2(self,nums):
        if not nums:
            return nums
        nums_str = list(map(str,nums))
        for i in range(1,len(nums_str)):
            j = i
            while j > 0:
                if nums_str[j-1] + nums_str[j]>nums_str[j] + nums_str[j-1]:
                    break
                else:
                    nums_str[j - 1], nums_str[j] = nums_str[j], nums_str[j - 1]
                    j -= 1
        res = ''.join(nums_str)
        if res[0] == '0':
            res = '0'
        return res
if __name__ =='__main__':
    h = Solution()
    nums =[3,30,34,5,9]
    result = h.lagerstnum2(nums)
    print(result)
