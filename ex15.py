#导入argv
from sys import argv
#提供输入参数：脚本文件、待打开文件
script, filename = argv
#打开文件
txt = open(filename)
#打印文件名
print "Here's your file %r:" % filename
#读取文件内容到内存
print txt.read()
#提示：再次打开文件
print "Type the filename again:"
#提示输入文件名
file_again = raw_input("> ")
#根据输入的文件名打开文件
txt_again = open(file_again)
#打印文件内容
print txt_again.read()