import heapq

def euc(x:int, y:int) -> Tuple[float, int, int]:
  return ((x**2 + y**2)**0.5, x, y)

class Solution:
  def kClosest(self, points: List[List[int]], k:int) -> List[List[int]]:
    points = [euc(el[0], el[1]) for el in points]
    heapq.heapify(points)
    res = []
    for _ in range(k):
      _, x, y = heapq.heappop(points)
      res.append([x,y])
    return res
