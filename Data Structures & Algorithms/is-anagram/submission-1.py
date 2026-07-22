class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(t)!=len(s):
      return False
    count = [0]*26 # [0,0,0… 0] len 26
    val_a = ord('a')
    for a,b in zip(s,t):
      count[ord(a) - val_a] += 1
      count[ord(b) - val_a] -= 1
    return not any(count)
