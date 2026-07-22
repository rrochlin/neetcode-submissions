class Solution:
  def breakIntoDict(self, string: str) -> Dict[str, int]:
    res = {}
    for s in string:
      res[s] = res.get(s, 0) + 1
    return res

  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = []
    result = []
    for s in strs:
      d = self.breakIntoDict(s)
      i = 0
      while i < len(anagrams):
        if anagrams[i] == d:
          result[i].append(s)
          break
        i += 1
      if i == len(anagrams):
        anagrams.append(d)
        result.append([s])
    return result
