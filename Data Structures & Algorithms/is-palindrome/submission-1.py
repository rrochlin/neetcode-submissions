import re

class Solution:
  def isPalindrome(self, s: str) -> bool:
    cleaned = re.sub(r"[^A-Za-z0-9]", "", s) # something like this
    left = 0
    right = len(cleaned) - 1
    while left < right:
      if cleaned[left].lower() != cleaned[right].lower():
        return False
      left += 1
      right -= 1
    return True
