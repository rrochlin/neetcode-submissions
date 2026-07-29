class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    left = {'(', '{', '['}
    right = {')':'(', '}': '{', ']': '['}
    for c in s[::]:
      if c in left:
        stack.append(c)
        continue
      if len(stack)==0 or stack[-1] != right[c]:
        return False
      stack.pop()
    return len(stack)==0
