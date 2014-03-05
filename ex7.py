#打印'Mary had a little lamb.'
print "Mary had a little lamb."
#打印‘Its fleece was white as snow’
print "Its fleece was white as %s." % 'snow'
#打印‘And everywhere that Mary went.’
print "And everywhere that Mary went."
#打印‘..........’
print "." * 10 # what'd that do?
#给end1~end12赋值
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# watch that comma at the end. try removing it t
#打印‘cheese’默认多打印一个换行
print end1 + end2 + end3 + end4 + end5 + end6
#打印‘Burger’默认多打印一个换行
print end7 + end8 + end9 + end10 + end11 + end12

#打印‘cheese’默认多打印一个换行，最后加‘,’，不会打印换行
print end1 + end2 + end3 + end4 + end5 + end6,
#打印‘Burger’
print end7 + end8 + end9 + end10 + end11 + end12
#最终结果‘cheese Burger’