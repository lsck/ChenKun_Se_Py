#coding=utf8
class Fish(object):
    def Juge_fish(self):
        Limbs=raw_input(u'它的四肢是什么？')
        Respiration=raw_input('它用什么呼吸')
        Live=raw_input('它生活在哪？')

        if Limbs=='Fin' and Respiration=='Bill' and Live=='in the water' :
            print u'通过观察发现：它生活在%s,它用%s来呼吸，四肢长的是%s'\
            %(Live,Respiration,Limbs)
            Juge_resault=u'初步判断结果：这是一条鱼。'
            print Juge_resault
            return 'Juge_resault'
        else:
            other=u'初步判断结果：这不是一条鱼。'
            print other
            return 'other'

class Loach(Fish):
    def Juge_loach(self):
        print u'首先，我们来看下这是不是一条鱼。'
        Juge_fish=Fish().Juge_fish()
        Body=raw_input(u'它的身型是什么样？')
        Beard=raw_input(u'它有胡须吗？')
        Hobbies=raw_input(u'它有什么爱好？')



        if Juge_fish=='Juge_resault':
            if Body=='Thin strip' and Beard=='The beard' and Hobbies=='Drilling mud' :
                print u'最终判断结果：这不仅是一条鱼，它还是一条泥鳅。'
            else:
                print u'最终判断结果：这算是一条鱼，但不是泥鳅。'
        else:
            print u'初步判断时,发现它不是一条鱼，所以我不知道它是什么东东。'

Loach().Juge_loach()




