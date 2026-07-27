class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set(nums)
        nums = list(nums)
        if len(new) == len(nums):
            return False
        else:
            return True