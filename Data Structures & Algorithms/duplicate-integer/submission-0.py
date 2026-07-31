class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set(nums)
        return new == nums