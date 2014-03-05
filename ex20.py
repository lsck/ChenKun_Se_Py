#导入argv
from sys import argv
#定义输入参数：脚本文件、待打开文件
script, input_file = argv
#定义函数：打印文件内容
def print_all(f):
    print f.read()
#定义函数：光标返回文件第1行
def rewind(f):
    f.seek(0)
#定义函数：根据行数打印文件内容
def print_a_line(line_count, f):
    print line_count, f.readline()
#打开文件
current_file = open(input_file)
#打印刚打开的文件
print "First let's print the whole file:\n"
print_all(current_file)
#将光标返回文件第一行
print "Now let's rewind, kind of like a tape."
rewind(current_file)
print "Let's print three lines:"
#定义行数，默认为1，打印第1行内容
current_line = 1
print_a_line(current_line, current_file)
#行数+1，打印第2行内容
current_line = current_line + 1
print_a_line(current_line, current_file)
#行数+1，打印第3行内容
current_line = current_line + 1
print_a_line(current_line, current_file)
