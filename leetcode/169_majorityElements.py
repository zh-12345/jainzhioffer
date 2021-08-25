class Solution():
    def majorityElement(self,nums):
        if len(nums) <0:
            return 0
        dict ={}
        i = 0
        while i<len(nums):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] =1
            i += 1
        for key, value in dict.items():
            if value > len(nums) // 2:
                return key

    def majorityElement2(self, nums):
        if len(nums) <= 0:
            return 0
        time =0
        for num in nums:
            if time ==0 :
                result = num
                time += 1
            elif num == result:
                time += 1
            else :
                time -=1
        def CheckMoreThanHalf(numbers, len, number):
            times = 0
            for i in range(len):
                if numbers[i] == number:
                    times += 1
            isMoreThanHalf = False
            if times * 2 > len:
                isMoreThanHalf = True
            return isMoreThanHalf

        if CheckMoreThanHalf(nums, len(nums), result):
            return result
        else:
            return 0
if __name__=='__main__':
    h= Solution()
    nums =[2,2,1,1,1,2,2]
    result = h.majorityElement2(nums)
    print(result)