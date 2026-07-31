class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            big = max(arr[i:])
            if arr[i] < max(arr[i:]) and i < arr.index(big):
                arr[i] = max(arr[i:])
        return arr
