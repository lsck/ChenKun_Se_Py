#����argv
from sys import argv
#��������������ű��ļ��������ļ�
script, input_file = argv
#���庯������ӡ�ļ�����
def print_all(f):
    print f.read()
#���庯������귵���ļ���1��
def rewind(f):
    f.seek(0)
#���庯��������������ӡ�ļ�����
def print_a_line(line_count, f):
    print line_count, f.readline()
#���ļ�
current_file = open(input_file)
#��ӡ�մ򿪵��ļ�
print "First let's print the whole file:\n"
print_all(current_file)
#����귵���ļ���һ��
print "Now let's rewind, kind of like a tape."
rewind(current_file)
print "Let's print three lines:"
#����������Ĭ��Ϊ1����ӡ��1������
current_line = 1
print_a_line(current_line, current_file)
#����+1����ӡ��2������
current_line = current_line + 1
print_a_line(current_line, current_file)
#����+1����ӡ��3������
current_line = current_line + 1
print_a_line(current_line, current_file)
