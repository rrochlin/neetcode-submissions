class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    if len(prices) == 1:
      return 0
    res = 0
    l = 0
    r = 1
    while len(prices) > r:
      if prices[r]-prices[l] > 0:
        res = max(res, prices[r]-prices[l])
      elif prices[r]-prices[l] < 0:
        l = r
      r+=1
    return res
