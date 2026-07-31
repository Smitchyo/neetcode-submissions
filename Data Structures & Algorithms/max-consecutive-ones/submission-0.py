class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if count > max:
                max = count
        return max