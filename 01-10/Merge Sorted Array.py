class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        sorted_list = list()
        p1 = 0
        p2 = 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted_list.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted_list.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted_list.append(nums1[p1])
                p1 += 1
            else:
                sorted_list.append(nums2[p2])
                p2 += 1

        nums1[:] = sorted_list


class Solution2(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        nums1.sort()