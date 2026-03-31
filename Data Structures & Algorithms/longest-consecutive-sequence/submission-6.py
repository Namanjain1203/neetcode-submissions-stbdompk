class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                current = num 
                count = 1
                while current + 1 in num_set:
                    current+=1
                    count+=1
                longest = max(longest,max)
        return langest
#        nums = sorted(set(nums)) 
#        longest = 1
#        current = 1
#        if not nums:
#            return 0
#
#        for i in range(len(nums)): 
#            if nums[i] == nums[i-1] + 1:
#                current += 1
#                longest = max(longest, current)
#            else:
#                current = 1  
#
#        return longest
