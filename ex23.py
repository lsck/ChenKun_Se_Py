#coding=utf-8
#---ͳ�Ƹ����ַ����������---
str=list(raw_input('�������ַ���:'))
i=0
str1=[]
str2=[]
str3=[]
str4=[]
while i <len(str):

    if str[i] in '0123456789':  
        str1.append(str[i])
        i=i+1
    elif str[i] in 'abcdefghijklmnopqrstuvwxyz':
        str2.append(str[i])
        i=i+1
    elif str[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        str3.append(str[i])
        i=i+1
    else :
        str4.append(str[i])
        i=i+1

print '��һ��������',len(str),'���ַ���'
print '\n'
print '����,'
print '����      �֡�:'+'[',len(str1),']����'
print '��СдӢ����ĸ��:'+'[',len(str2),']����'
print '����дӢ����ĸ��:'+'[',len(str3),']����'
print '���� �� �� ����:'+'[',len(str4),']����'
print '\n'

if len(str1)==0:
    print '����       �֡�:'
else :
    print '����       �֡�:',str1
    print '\n'
    
if len(str2)==0:
    print '��СдӢ����ĸ��:'
else :
    print '��СдӢ����ĸ��:',str2
    print '\n'
    
if len(str3)==0:
    print '����дӢ����ĸ��:'
else :
    print '����дӢ����ĸ��:',str3
    print '\n'
    
if len(str4)==0:
    print '���� �� �� ����:'
else :
    print '���� �� �� ����:',str4