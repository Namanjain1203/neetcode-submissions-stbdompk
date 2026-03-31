class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            seen.add(nums[i])
        if nums[i] in seen:
            return True
        else:
            return False 