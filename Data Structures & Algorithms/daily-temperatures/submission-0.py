class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    stack = []
    result = [0]*len(temperatures)
    for idx, t in enumerate(temperatures):
      while stack and t > stack[-1][0]:
        el = stack.pop()
        result[el[1]] = idx-el[1]
      stack.append((t, idx))
    return result
