#coding=utf-8
import xlrd
import show_menu
import machine_choose_dish
import human_choose_dish

class Control(object):
    def runner(self):
        a=[]
        num=0
        #调用显示菜单方法，显示整个菜单
        show_menu.show_xls().show_xls_menu()

        while num<3:
            try:
                object_mode=raw_input(u'看完菜单，手选还是机选？手选输1，机选输0。')
                if int(object_mode)==1:
                    print u'你选择了手选模式点菜，输入分类、菜肴序号即可。'
                    #调用手动选菜方法
                    human_choose_dish.human_choose().human_choose_xls_classify()
                    num+=1

                elif int(object_mode)==0:
                    print u'你选择了机选模式点菜，输入分类后，由程序随机选择菜肴序号。'
                    #调用系统随机选菜方法
                    machine_choose_dish.machine_choose().machine_choose_xls_classify()
                    num+=1
                else:
                    print u'只能输入数字1或0！'
            except (ValueError,TypeError):
                print u'请输入数字1或0！'


Control().runner()
