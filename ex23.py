#coding=utf-8
#---统计各类字符个数并输出---
str=list(raw_input('请输入字符串:'))
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

print '你一共输入了',len(str),'个字符。'
print '\n'
print '其中,'
print '【数      字】:'+'[',len(str1),']个。'
print '【小写英文字母】:'+'[',len(str2),']个。'
print '【大写英文字母】:'+'[',len(str3),']个。'
print '【其 他 字 符】:'+'[',len(str4),']个。'
print '\n'

if len(str1)==0:
    print '【数       字】:'
else :
    print '【数       字】:',str1
    print '\n'
    
if len(str2)==0:
    print '【小写英文字母】:'
else :
    print '【小写英文字母】:',str2
    print '\n'
    
if len(str3)==0:
    print '【大写英文字母】:'
else :
    print '【大写英文字母】:',str3
    print '\n'
    
if len(str4)==0:
    print '【其 他 字 符】:'
else :
    print '【其 他 字 符】:',str4