class Solution():
    def FindNumbersWithSum(self, data, length, sum):
        res = []
        if length < 0:
            return res
        ahead = 0
        behind = length - 1

        while behind > ahead:
            cursum = data[ahead] + data[behind]
            if cursum == sum:
                res.append(data[ahead])
                res.append(data[behind])
                break
            elif cursum > sum:
                behind -= 1
            else:
                ahead += 1
        return res

    def FindNumbersWithSum2(self, nums, target):
        res= []
        dict ={}
        if len(nums) <0:
            return res
        for i,n in enumerate(nums):
            find = target - n
            if find in dict.keys():
                res.append(find)
                res.append(n)
                return res
            dict[n] = i


if __name__ == "__main__":
  h = Solution()
  nums =[1,2,4,7,11,15]
  # result = h.FindNumbersWithSum(nums,6,15)
  result =h.FindNumbersWithSum2(nums,15)
  print(result)