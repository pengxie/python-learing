#!/bin/env python
# this one like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print"arg1: %r" % arg1

def print_none():
	print "I got nothing."

def print_interactive():
	print "your name:%r\nyour age:%r\n" % (raw_input("name:\n"),raw_input("age:\n"))

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
print_interactive()
