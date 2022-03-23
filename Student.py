#!/bin/python


class Student:

 # Constructor - student has a name
 def __init__(self, name):
  self.name = name
  self.parents = []
  self.address = ""

 def addparent(self, parentname):
  self.parents.append(parentname)

 def changeaddress(self, theaddress):
  self.address = theaddress

 def storeinfo(self):
  info = { self.name : {"parents": self.parents, 
                        "address": self.address} 
         }
  return info

