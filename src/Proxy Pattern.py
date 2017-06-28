'''
给某一个对象提供一个代理或占位符，
并由代理对象来控制对原对象的访问。
'''

from abc import ABCMeta, abstractmethod

class GiveGift:
    @abstractmethod
    def give_rose(self):
        pass
    @abstractmethod
    def give_chocolate(self):
        pass

class Persuit(GiveGift):
    def __init__(self,name):
        self.name = name
    def give_rose(self):
        print("Give rost to",self.name)
    def give_chocolate(self):
        print("Give chocolate to",self.name)

class Proxy(GiveGift):
    def __init__(self,name):
        self.person = Persuit(name);
    def give_rose(self):
        self.person.give_rose()
    def give_chocolate(self):
        self.person.give_chocolate()


Per = Proxy("Xiaoli")
Per.give_chocolate()
Per.give_rose()
