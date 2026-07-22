class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = {}
        for idx, num in enumerate(nums):
            if num in solution:
               return [solution[num], idx]
            solution[target-num] = idx
        return []
