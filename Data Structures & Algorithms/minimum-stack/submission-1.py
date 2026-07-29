class MinStack:

  def __init__(self):
    self.stack = []
    self.minS = []
    self.minEl = 2**31
        
  def push(self, val: int) -> None:
    self.stack.append(val)
    if val < self.minEl:
      self.minEl = val
      self.minS.append(val)
    else:
      self.minS.append(self.minS[-1])
        
  def pop(self) -> None:
    self.stack.pop()
    self.minS.pop()
    if len(self.minS)==0:
      self.minEl = 2**31
    else:
      self.minEl = self.minS[-1]
        
  def top(self) -> int:
    return self.stack[-1]
        
  def getMin(self) -> int:
    return self.minEl
