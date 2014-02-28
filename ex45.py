#coding=utf-8
import xlrd

def show_xls():
    #打开xls
    file = xlrd.open_workbook('D:\\menu.xls')
    #获取xls的所有sheet页名称
    sheet_name=file.sheet_names()

    #迭代打开各sheet页
    for i in range(len(sheet_name)):
        #按序号打开sheet页
        sheet = file.sheet_by_index(i)
        #获得sheet页的行数
        nrows = sheet.nrows
        #获得sheet页的列数
        ncols = sheet.ncols
        #打印Sheet页名称
        print '-----%s-----' %sheet_name[i]
        #迭代获取Sheet页的各行数据
        for i in range(sheet.nrows):
            row_value=list(sheet.row_values(i))
            #迭代打印Sheet页的各行数据
            for i in range(len(row_value)):
                '''if isinstance(row_value[i],float)==True:
                    row_value[i]=int(row_value[i])
                else:
                    pass'''
                print row_value[i],
            #每行输出完后打印一个空行，换行作用
            print
        #每Sheet页输出完后打印一个空行，换行作用
        print

def Artificial_choose_xls_rows(classify):
    a=1
    while a==1:
        file=xlrd.open_workbook('D:\\menu.xls')
        sheet = file.sheet_by_index(classify)
        xls_sheet_name=file.sheet_names()
        nrows = sheet.nrows
        ncols = sheet.ncols

        try :
            dish_num=int(raw_input(u'请输入菜肴序号:'))
            if dish_num in range(nrows):
                num,name,value= sheet.row_values(dish_num)
                print num,name,value
                a=0
            else:
                raise IndexError
        except (ValueError,TypeError):
            print u'菜肴序号只能输入数字!'
        except (IndexError):
            print u'输入的菜肴序号超出上限,请重新输入!'
    return num,name,value

def Artificial_choose_xls_classify():
    #打开xls
    file = xlrd.open_workbook('D:\\menu.xls')
    #获取xls的所有sheet页名称
    sheet_name=file.sheet_names()
    a=1
    while a==1:
            try:
                classify=int(raw_input(u'请选择分类：'))
                if classify in range(len(sheet_name)):
                    sheet = file.sheet_by_index(classify)
                    print u'你选择的分类是：%s' %sheet_name[classify]
                    Artificial_choose_xls_rows(classify)
                    a=0
                else:
                    raise IndexError
            except (ValueError,TypeError):
                print u'分类只能输入数字！'
            except (IndexError):
                print u'输入的分类超出上限,请重新输入！'
show_xls()

num=1
while num==1:
    try:
        object_mode=raw_input(u'看完菜单，手选还是机选？手选输1，机选输0。')
        if int(object_mode)==1:
            print u'你选择了手选模式点菜，输入分类、菜肴序号即可。'
            Artificial_choose_xls_classify()
            num=0
        elif int(object_mode)==0:
            print u'你选择了机选模式点菜，输入分类后，由程序随机选择菜肴序号。'
            
        else:
            print u'只能输入数字1或0！'
    except (ValueError,TypeError):
        print u'请输入数字1或0！'


