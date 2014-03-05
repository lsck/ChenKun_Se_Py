#coding=utf-8
formatter="%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ('One','Two','Three','Four')
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)

print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight.",
    )
print

#单引号跟双引号混合时，要么单引号包含双引号，要么双引号包含单引号，否则会报错

#例1：单引号包含双引号
print u'我是"中国人"'

#例2：双引号包含单引号
print u"我是‘中国人’"

#EOF报错
#print u"我是'中国人"'
#print u'我是"中国人'"
