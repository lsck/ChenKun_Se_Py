#coding=utf-8
import xlrd
class human_choose(object):
    def human_choose_xls_rows(self,classify):

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
                    print u'你选择的菜肴是：%s %s %s' %(int(num),name,value)
                    a=0
                else:
                    raise IndexError
            except (ValueError,TypeError):
                print u'菜肴序号只能输入数字!'
            except (IndexError):
                print u'输入的菜肴序号超出上限,请重新输入!'


    def human_choose_xls_classify(self):
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
                        human_choose().human_choose_xls_rows(classify)
                        a=0
                    else:
                        raise IndexError
                except (ValueError,TypeError):
                    print u'分类只能输入数字！'
                except (IndexError):
                    print u'输入的分类超出上限,请重新输入！'

human_choose().human_choose_xls_classify()
