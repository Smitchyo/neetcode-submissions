class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set(nums)
        if new != nums:
            return True
        else:
            return False