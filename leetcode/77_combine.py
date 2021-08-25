class Solution():
    def combine(self,n,k):
        def backtrack(track,n,k,level):
            if len(track)== k:
                self.res.append(track[:])
                return
            for i in range(level,n+1):
                # if i in track:
                #     continue
                track.append(i)
                backtrack(track,n,k,i+1)
                track.pop()
        self.res =[]
        track =[]
        backtrack(track,n,k,1)
        return self.res
if __name__=='__main__':
    h =Solution()
    n = 4
    k =2
    result =h.combine(n,k)
    print(result)