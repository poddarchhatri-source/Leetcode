class Solution:
    def findLHS(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        maxCount = 0
        for i in range(n):
            Min = nums[i]
            count = 0
            for j in range(i+1,n):
                Max =  nums[j]
                if Max-Min == 1:
                    maxCount = max(maxCount,j-i+1)
                elif Max-Min>1 :
                    break
        return maxCount
