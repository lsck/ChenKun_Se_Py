#coding=utf-8
import random

#定义计数器，默认为0
num=01
1
#定义随机结果集，默认为空列表
choose_resault=[]

#最多可随机5次
while num<5:
    #输入上下限

    min_num = input(u'随机数下限：')
    max_num = input(u'随机数上限：')

    #确定上限必须大于下限
    if min_num>=max_num:
        print u'随机数上限必须大于下限'
        pass
    #确定能随机5次
    elif len(range(min_num,max_num+1))<5:
        print u'随机数总数小于5，不够随机5次，重新输入！'
        pass
    else:
    #根据上下限生成列表
        random_list=range(min_num,max_num+1)
        print u'根据您输入的上下限，已准备好从%d到%d共计%d个随机数可抽取！' %(min_num,max_num,len(range(min_num,max_num+1)))
        #最多可随机5次

        while num<5:
            #确定是否随机？
            choose=int(raw_input(u'是否随机抽取一个？(‘是’则1，‘否’则0)'))
            #输入1，生成随机数
            if choose==1:
                #根据列表生成随机数
                random_num=random.choice(random_list)
                #判断随机数是否已存在于随机结果集，不存在则添加，计数器+1，存在则提示重复
                if random_num not in choose_resault:
                    choose_resault.append(random_num)
                    print u'第%d次随机结果：%d' %(num+1,random_num)
                    num+=1
                else:
                    print u'第%d次随机结果：%d，重复，需重新随机一次！' %(num+1,random_num)
                    pass
            #输入0，程序退出，并给出提示
            elif choose==0:
                print u'你在第%d次随机时选择了退出！' %(num+1)
                num=6
                break
            #输入非1、0，给出提示
            else:
                print u'请输入1或0！'

#计数器为5，程序退出
while num==5:
    #随机5次，程序退出
    print u'随机次数已达5次，程序退出！'
    print u'最终随机结果如下：',choose_resault
    break
#计数器不为0~5，打印也已随机的结果
else:
    print u'最终随机结果如下：',choose_resault
