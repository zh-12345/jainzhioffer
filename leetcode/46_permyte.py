class Solution():
    def permute(self, nums):
        def backtrack(nums, track):
            if len(track) == len(nums):
                self.res.append(track[:])
                return
            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                backtrack(nums, track)
                track.pop()

        self.res = []
        track = []
        backtrack(nums, track)
        return self.res




if __name__ == '__main__':
    h =Solution()
    nums=[1,2,3]
    li = h.permute(nums)
    print(li)