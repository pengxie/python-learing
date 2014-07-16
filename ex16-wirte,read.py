# -*- coding: utf-8 -*-
from sys import argv
script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETUN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'rw+') # open mode "a" 追加；'w'写；“r” 读，默认的打开的文件是文本模式，以"\n"
# 为区分符，如果是二进制文件，需要指定 ‘b’参数

print "Truncating the file. Goodbye!"
target.truncate()   
# truncate方法清空

print "I'm going to write these to file."

target.write("xiepeng") # 写入文件
target.write("\n")
target.write("Shanghai")
target.write("\n")
target.write("Benjing")
target.write("\n")


print "And finally, we clonse it."

target.close() # 关闭文本

file1 = open(filename)
for i in file1.read():
 print i

print "aaaaaaaaaaaaaaaaaaaaaaaaa"
line = file1.readline(2)
print "a:%s" % line
file1.close()
