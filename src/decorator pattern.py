'''
动态地给一个对象添加一些额外的职责，就增加功能来说，装饰模式比生成子类更加灵活
装饰模式是一种对象结构型模式
'''

from abc import ABCMeta, abstractmethod


class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print (self.name)


# decorator class
class Clothes(Person):
    def __init__(self):
        pass

    def Decorate(self,component):
        self.component = component

    def show(self):
        self.component.show()

class Shoes(Clothes):
    def __init__(self):
        pass

    def show(self):
        print ("shoes get ")
        self.component.show()


class Necklace(Clothes):
    def __init__(self):
        pass

    def show(self):
        print ("Necklace get ")
        self.component.show()


P = Person("wenfeng")
S = Shoes()
N = Necklace()

S.Decorate(P)
N.Decorate(S)
N.show()
