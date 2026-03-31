class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n):
            target = -nums[i]
            seen = set()
            for j in range(i + 1, n):
                if target - nums[j] in seen:
                    res.add((nums[i], target - nums[j], nums[j]))
                seen.add(nums[j])
        return [list(triplet) for triplet in res]
   