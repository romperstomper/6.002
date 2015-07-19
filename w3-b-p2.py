#!/usr/bin/python
import random
import re


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
    if self.getClearProb < self.prob:
      return False
    return True

  def reproduce(self, popDensity):
    if self.maxBirthProb*(1-popDensity) > self.prob:
      return SimpleVirus(self.maxBirthProb, self.getClearProb)
    raise NoChildException

class Patient(object):
  def __init__(self, virus, numtrials):
    self.viruses = virus
    self.numtrials = numtrials
    self.max_virus_pop = 101

  def update(self):
    for virus in self.viruses:
      if virus.doesClear():
	self.viruses.remove(virus)
        
    for virus in self.viruses:
      popDensity = len(self.viruses)/self.max_virus_pop
      try:
        new_virus = virus.reproduce(popDensity)
	self.viruses.append(new_virus)
      except NoChildException:
	pass
    return len(self.viruses)

  def getTotalPop(self):
    return len(self.viruses)
    for i in range(self.numtrials):
      self.update()

