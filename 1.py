# -*-coding: utf8 -*-
from sys import argv
script,filename = argv
with open(filename,'r') as file:
  data = file.readlines()
  print data
  for line in data:
        words = line.split()
        print words
