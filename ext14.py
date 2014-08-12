# -*- coding: utf-8 -*- 
from sys import argv

script, user_name = argv #一个变量为脚本名，二为第一个变量名
prompt = 'ubuntu@localhost:  '
print type(prompt)

print "%s" % (script)
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "what kind of computer do you hava?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %s. Not sure where that is.
And you have %r computer. Nice.
""" % (likes, lives, computer)
