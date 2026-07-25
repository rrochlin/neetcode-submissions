class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    res = []
    for i in range(len(nums)-2):
      if i>0 and nums[i-1]==nums[i]:
        continue
      l = i+1
      r = len(nums)-1
      while l<r:
        total = nums[l]+nums[r]+nums[i]
        if total > 0:
          r-=1
        elif total < 0:
          l+=1
        else:
          res.append([nums[i],nums[l],nums[r]])
          l+=1
          r-=1
          while l<r and nums[l-1]==nums[l]:
            l+=1
    return res
