#coding=utf-8
# Here's some new strange stuff, remember type it exactly.
days = "Mon Tue Wed Thu Fri Sat Sun"
#\n转义换行
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Here are the days: ",days
print "Here are the months: ", months
#三引号，可以直接打印中间的其他字符，不需转义
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
#'+'拼接字符串时，两字符串之间没有空格，
print 'a'+'b'
#','拼接字符串时，中间会打印一个空格
print 'a','b'