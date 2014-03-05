#coding=utf-8
##定义动物类
class Animal(object):
    #无任何执行语句，pss
    pass
## 定义狗类
class Dog(Animal):
    def __init__(self, name):
        ## 初始化name
        self.name = name
## 定义猫类
class Cat(Animal):
    def __init__(self, name):
        ## 初始化name
        self.name = name
## 定义人类
class Person(object):
    def __init__(self, name):
        ## 初始化name
        self.name = name
        ## 初始化宠物=none
        self.pet = None
## 定义员工类，员工类继承自人类
class Employee(Person):
    def __init__(self, name, salary):
    ## 调用‘人类’的方法初始化name
        super(Employee, self).__init__(name)
        ## 初始化工资
        self.salary = salary
## 定义鱼类
class Fish(object):
    pass
## 定义大马哈鱼类
class Salmon(Fish):
    pass
## 大比目鱼
class Halibut(Fish):
    pass
## 调用狗类
rover = Dog("Rover")
## 调用猫类
satan = Cat("Satan")
## 调用人类
mary = Person("Mary")