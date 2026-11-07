class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return i
        if nums[0]>target :
            return 0
        for i in range(n-1):
            if nums[i]<target and nums[i+1]>target:
                return i+1

        return n