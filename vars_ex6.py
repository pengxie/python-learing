#/bin/env/python
# -- coding: utf-8 -- 
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)

print x
print y

print "I said: %r." % x  # %r 按照repr()的对象来返回数据，同时对于字符串返回的值带有''.
print "I also said: '%s'." % y # %s 按照str()的对象返回

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."

print w + e  #连接符
