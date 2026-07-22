class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        runsum = 0
        prev = 0
        for num in nums:
            if num > prev:
                runsum += num
                prev = num
                continue
            prev = num
            if runsum > res:
                res = runsum
            runsum = num
        if runsum > res:
            return runsum
        return res

        