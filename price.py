#!/bin/env python
width = input('plase enter width:')
price_width = 10
item_width = width - price_width
print item_width
header_format = '%-*s%*s'
format = '%-*s%*.2f' # - left * allow you input canshu
print '=' * width
print header_format % (item_width, 'Item',price_width,'price')
print '-' * width
print format % (item_width, 'Apples',price_width, 0.4)
print format % (item_width, 'Pears', price_width, 0.5)
print '=' * width
