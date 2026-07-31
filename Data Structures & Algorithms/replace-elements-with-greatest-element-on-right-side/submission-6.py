class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1, -1, -1):
            big = -1
            current = arr[i]
            arr[i] = big
            biggest = max(big,current)
        return arr
