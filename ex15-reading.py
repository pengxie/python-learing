# -*- coding: utf8 -*-
from sys import argv
script, filename = argv
txt = open(filename)  # 打开文件

print "Here's you file %r:" % filename
print txt.read() # 读取整个文件的内容

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
