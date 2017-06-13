'''
定义一系列算法，将每一个算法封装起来，并让它们可以相互替换，策略模式独立于使用它的客户
而变化，也称为政策模式。策略模式是一种对象行为型模式
'''

from abc import ABCMeta, abstractmethod

class cash_super:
    def __init__(self,x):
        self.money = x

    @abstractmethod
    def get_result(self):
        pass

class cash_normal(cash_super):
    def get_result(self):
        return self.money

class cash_disconnt(cash_super):
    def __init__(self,x,dis):
        cash_super.__init__(self,x)
        self.discount = dis

    def get_result(self):
        return self.money*self.discount

class cash_context:
    def __init__(self,type,x,dis):
        if type=="Normal":
            self.cs = cash_normal(x)
        else:
            self.cs = cash_disconnt(x,dis)
    def get_money(self):
        return self.cs.get_result()


cs1 = cash_context("Normal",1000,0)
cs2 = cash_context("Discount",1000,0.8)
print cs1.get_money()
print cs2.get_money()
