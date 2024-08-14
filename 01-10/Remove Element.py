class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index = index +1
        return index


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        left =0
        right = len(nums)
        while (left < right):
            if nums[left] == val:
                nums[left] = nums[right-1]
                right = right - 1
            else:
                left = left + 1
        return left