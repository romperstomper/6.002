# Enter your definition for the ResistantVirus class in this box.
# You'll enter your code for TreatedPatient on the next page.
class ResistantVirus(SimpleVirus):
  def __init__(self, maxbirthprob, getclearprob, resdict, mutprob):
    SimpleVirus.__init__(self, maxbirthprob, getclearprob)
    self.resdict = resdict
    self.mutprob = mutprob
    self.getclearprob = getclearprob
    self.maxbirthprob = maxbirthprob
    
  def isResistantTo(self, drug):
    return self.resdict.get(drug)
    
  def reproduce(self, popDensity, drugtreatment):
    inherit = {}
    for drug in drugtreatment:
      if not self.resdict[drug]:
        raise NoChildException
    for res in self.resdict:
      if random.random() > self.mutprob:
        inherit[res]= self.resdict[res]
      else:
        inherit[res]= not self.resdict[res]

    if random.random() < self.maxbirthprob*(1-popDensity):
      return ResistantVirus(self.maxbirthprob, self.getclearprob, inherit, self.mutprob)
    raise NoChildException



