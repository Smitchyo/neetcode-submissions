class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in nmap:
                return [nmap[compliment],i]
            nmap[num] = i
        return []