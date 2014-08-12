#/bin/env python
# -*- coding: utf-8 -*-
# * 和 **的区别，* 是代表所有的值，而**这是将前面的值作为主健来进行遍历

def print_everything(*args):
	print type(args)
 	for count, thing in enumerate(args):
         print "{0}. {1}".format(count,thing) # format str的内置函数，用count的值替换{0}的值，thing替换后面的{1}
def table_things(**kwargs):
	print type(kwargs)
	print kwargs
	print kwargs.keys()
	print kwargs.values()
	print kwargs.items()
	print kwargs.iteritems()
 	for name, value in \
 	    kwargs.items():
         print "{0} = {1}".format(name, value)

print_everything('apple','bana','cabbage')
table_things(apple = 'fruit', cabbage = 'vegetable')

def print_three_things(a, b, c):
    print 'a = {0}, b = {1}, c = {2}'.format(a,b,c)

mylist = ['aardvark', 'baboon', 'cat']
print_three_things(*mylist)

test = ((1,'xiepeng'),(2,'leifang'))
print dict((y,x) for x, y in test)

a = (1,2,3,4,5)
b = [1,2,3,4,5]
c = {"xiepeng":12, "xie":22, "peng":23}
print type(a)
print type(b)
print type(c)
del b[2]
b.append(6)
c["xiexie"] = 24
print type(c.has_key('xiepeng'))
print c.values()

