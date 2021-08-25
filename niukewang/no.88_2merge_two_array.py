class Solution:
    def sort(self, a, b):
        # write code here

        n = len(b)
        m = len(a)
        a = a + [0] * n
        cur = k = m - 1
        for i in range(0, n):
            if a[k] < b[i]:
                a[m + n -1- i] = b[i]
            else:
                while cur >= 0 and a[cur] > b[i]:
                    cur -= 1
                for j in range(k, cur, -1):
                    a[j + 1] = a[j]
                a[cur + 1] = b[i]
                k += 1
        return a

if __name__ == "__main__":
    h = Solution()
    # nums1 = [0]
    # nums2 = [2]
    # nums1 = [1,2,3,0,0,0]
    # nums2 = [2,5,6]
    nums1 = [0, 2, 4]
    nums2 = [5, 3, 1]
    # nums1 = h.merge_two_array1(nums1, 3, nums2,len(nums2))
    nums1 = h.sort(nums1,  nums2)
    print(nums1)