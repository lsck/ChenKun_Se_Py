#����argv
from sys import argv
#�ṩ����������ű��ļ��������ļ�
script, filename = argv
#���ļ�
txt = open(filename)
#��ӡ�ļ���
print "Here's your file %r:" % filename
#��ȡ�ļ����ݵ��ڴ�
print txt.read()
#��ʾ���ٴδ��ļ�
print "Type the filename again:"
#��ʾ�����ļ���
file_again = raw_input("> ")
#����������ļ������ļ�
txt_again = open(file_again)
#��ӡ�ļ�����
print txt_again.read()