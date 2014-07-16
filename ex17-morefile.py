# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists 
#exists判断文件是否存在，返回值为bool类型
script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "type:%r " % type(exists(to_file)) #查看返回类型
print "=" * 10
print "Ths input file is %d bytes long" % len(indata) #查看字节长度
print "Does the output file exists? %r" % exists(to_file)
print "Ready, hist REUTRN to continue. CTRL-C to absort."
raw_input()

out_file = open(to_file,'w')
out_file.write(indata) 

print "Alright, all done."

out_file.close()
in_file.close()
