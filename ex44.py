#coding=utf-8
class Parent(object):
    def implicit(self):
        print "This is %s's PARENT implicit()" % self

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
