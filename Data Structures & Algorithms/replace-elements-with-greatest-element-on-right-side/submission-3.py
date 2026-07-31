class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == 0:
                big = max(arr[i:])
            else:
                big = max(arr[i-1:])
            if arr[i] < max(arr[i:]) and i < arr.index(big):
                arr[i] = max(arr[i:])
        arr[-1] = -1
        return arr
