class Solution():
    def findRepeatNum(self,nums,length):
        if length < 0:
            return -1
        start = 1
        end = length -1
        def countrange(numbers,length,start, end):
            if length < 0:
                return 0
            count =0
            for i in range(length):
                if numbers[i] >=start and numbers[i]<=end:
                    count += 1
            return count
        while start <= start:
            middle = (end -start)//2 + start
            count = countrange(nums,length,start,middle)
            if end == start:
                if count >1:
                    return start
                else:
                     break
            if count > middle-start+1:
                end = middle
            else:
                start= middle+1
        return -1

if __name__=="__main__":
    h = Solution()
    nums=[2,3,5,4,3,2,6,7]
    result = h.findRepeatNum(nums,8)
    print(result)