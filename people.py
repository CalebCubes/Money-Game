import math

class Player:
  
  name = ''
  money = 0
  rev = 0

  def __init__(self, name):
    self.money = 5000
    self.rev = 100
    self.name = name

  def buyall(self,Rev,sub):
    awesomesub = self.money /sub
    getfloredsub = math.floor(awesomesub)
    print ('you bought %s '% getfloredsub,)
    nower = self.money
    self.money = nower - getfloredsub*sub
    now = self.rev
    self.rev = now + getfloredsub*Rev
  
  def buying(self,Rev,sub):
    if self.money >= sub:
      now = self.rev 
      self.rev = now + Rev 
      nower = self.money
      self.money = nower - sub