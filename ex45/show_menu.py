#coding=utf-8
import xlrd
class show_xls(object):

    def show_xls_menu(self):
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
                    #将小数转换为整数
                    if isinstance(row_value[i],float)==True:
                        row_value[i]=int(row_value[i])
                    else:
                        pass
                    #打印每行的每列数据
                    print row_value[i],
                #打印完一条数据后，换行
                print
            #打印完一个Sheet页后，换行
            print
        return 1
show_xls().show_xls_menu()
