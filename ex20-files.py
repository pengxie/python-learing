#!/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
script, intput_file = argv
def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)   #将索引定在第几行，这里是将索引还原

def print_a_line(line_count, f):
	print line_count, f.readline().strip('\n') #每一次readline()索引往下移一

current_file = open(intput_file)
print "Fiste let's print the whole file:"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's pint there lines:"
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
