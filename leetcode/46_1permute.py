class Solution():
    def permute(self, nums):
        def dfs(k,nums,track):
            if k==len(nums):
                res.append(track[:])
                return
            for i in range(len(nums)):
                if not visited[i]:
                    if i>0 and nums[i]==nums[i-1] and not visited[i-1]:
                        continue
                    visited[i]=True
                    track.append(nums[i])
                    dfs(k+1,nums,track)
                    visited[i]=False
                    track.pop()

        visited=[False]*len(nums)
        res=[]

        dfs(0,nums,[])
        return res







if __name__ == '__main__':
    h =Solution()
    nums=[1,1,1]
    li = h.permute(nums)
    print(li)