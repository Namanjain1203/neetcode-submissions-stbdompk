class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        return nums[0]