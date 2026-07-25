import heapq
from copy import deepcopy

class KthLargest:

  def __init__(self, k: int, nums: List[int]):
    self.k = k
    heapq.heapify_max(nums)
    self.heap = nums
    

  def add(self, val: int) -> int:
    heapq.heappush_max(self.heap, val)
    temp = deepcopy(self.heap) # might have to do deepcopy here
    for i in range(self.k-1):
      heapq.heappop_max(temp)
    return heapq.heappop_max(temp)
