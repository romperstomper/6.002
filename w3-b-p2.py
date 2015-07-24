#!/usr/bin/python
import random
import re

class NoChildException(Exception):
  pass

class SimpleVirus(object):
  def __init__(self, maxbirthprob, getclearprob):
    self.maxBirthProb = maxbirthprob
    self.getClearProb = getclearprob
    self.prob = 0

  def maxBirthProb(self):
    return self.maxbirthprob
  def getClearProb(self):
    return self.getclearprob

  def doesClear(self):
    self.prob = random.random()
    return self.prob < self.getClearProb

  def reproduce(self, popDensity):
    if self.prob < self.maxBirthProb*(1-popDensity):
      return SimpleVirus(self.maxBirthProb, self.getClearProb)
    raise NoChildException

class Patient(object):
  def __init__(self, virus, maxPop):
    self.viruses = virus
    self.max_virus_pop = maxPop

  def update(self):
    for virus in self.viruses:
      if virus.doesClear():
	self.viruses.remove(virus)
        
    for virus in self.viruses:
      popDensity = len(self.viruses)/float(self.max_virus_pop)
      try:
        new_virus = virus.reproduce(popDensity)
	self.viruses.append(new_virus)
      except NoChildException:
	pass
    return len(self.viruses)

  def getTotalPop(self):
    return len(self.viruses)

