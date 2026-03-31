class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        longest = 1
        current = 1
        for i in range(len(nums)):
            if nums[i]==nums[i-1]+1:
                current+=1
                longest = max(longest,current)
            else:
                current = 1
        return longest