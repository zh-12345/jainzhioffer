class Solution:
    def merge_two_array1(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 or j >= 0:
            if j == -1:
                nums1[k] = nums1[i]
                i -= 1
            elif i == -1:
                nums1[k] = nums2[j]
                j -= 1
            elif nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            elif nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                # k -= 1
                i -= 1
            k -= 1
        return nums1

    def merge_two_array2(self, nums1, m, nums2, n):
        cur = k = m - 1

        for i in range(n - 1, -1, -1):
            if nums1[k] < nums2[i]:
                nums1[m + i] = nums2[i]
            else:
                while cur >= 0 and nums1[cur] > nums2[i]:
                    cur -= 1
                for j in range(k, cur, -1):
                    nums1[j + 1] = nums1[j]
                nums1[cur + 1] = nums2[i]
                k += 1
        return nums1


if __name__ == "__main__":
    h = Solution()
    # nums1 = [0]
    # nums2 = [2]
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    # nums1 = [4, 5, 6, 0, 0, 0]
    # nums2 = [1, 2, 3]
    # nums1 = h.merge_two_array1(nums1, 3, nums2,len(nums2))
    nums1 = h.merge_two_array2(nums1, 3, nums2, len(nums2))
    print(nums1)
