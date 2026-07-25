import heapq

class KthLargest:

  def __init__(self, k: int, nums: List[int]):
    self.k = k
    heapq.heapify_max(nums)
    self.heap = nums
    

  def add(self, val: int) -> int:
    heapq.heappush_max(self.heap, val)
    temp = []
    for i in range(self.k-1):
      temp.append(heapq.heappop_max(self.heap))
    res = self.heap[0]
    for num in temp:
      heapq.heappush_max(self.heap, num)
    return res
