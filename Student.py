#!/bin/python

# class for Student datatype with attributes
 # name: string
 # parent's names: list of strings
 # address: string
class Student:

 # Constructor - student has a name
 def __init__(self, name):
  self.name = name
  self.parents = []
  self.address = ""
  #self.events = 

 def addparent(self, parentname):
  self.parents.append(parentname)

 def changeaddress(self, theaddress):
  self.address = theaddress

 # store it as a nested dictionary for database
 def storeinfo(self):
  info = { self.name : {"parents": self.parents, 
                        "address": self.address} 
         }
  return info


import json
import os

# implementation of the actual database
class StudentDB(object):

 def __init__(self, location):
  self.location = os.path.expanduser(location)
  self.load(self.location)

 # load the database if it exists
 # create a new one if it doesn't
 def load(self, location):
  if os.path.exists(location):
   print("DB exists, loading")
   self._load()
  else:
   print("DB doesn't exist, creating a new one")
   self.db = {}

 # private function to actually load the database
 def _load(self):
  self.db = json.load(open(self.location, "r"))

 # print the database in memory to file
 def updatedb(self):
  try:
   json.dump(self.db, open(self.location, "w+"))
  except:
   print("There was a problem with writing the database")
 
 # set a student into database
 def set(self, student):
  self.db.update(student)
  self.updatedb()

 # get a student dictionary from the database
 # return the correct Student object
 def getstudent(self, studentname):
  try:
   # get the dictionary
   studentdict = self.db[studentname]
   # initialize Student with student name
   thestudent = Student(studentname)
   # add address to Student
   thestudent.changeaddress(studentdict["address"])
   # add parent(s) to Student
   for p in studentdict["parents"]:
    thestudent.addparent(p)
   return thestudent
  except KeyError:
   print("The student {} does not exist".format(studentname))
   return False
  
  













