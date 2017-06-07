'''
定义一个工厂类，它可以根据参数的不同返回不同类的实例，被创建的实例通常具有相同的父类。
用于创建实例的方法是静态方法，因此简单工厂模式又称为静态工厂模式，属于类创建方法
'''


class operatoion:
    def __init__(self,numA = 0,numB = 0):
        self.numberA = numA
        self.numberB = numB
    def get_result(self):
        pass

class add(operatoion):
    def get_result(self):
        return self.numberA + self.numberB

class sub(operatoion):
    def get_result(self):
        return self.numberA - self.numberB

class mul(operatoion):
    def get_result(self):
        return self.numberA*self.numberB

class div(operatoion):
    def get_result(self):
        return self.numberA/self.numberB

class operation_factory:

    @staticmethod               # static method don't need self
    def get_operation(op):
        if op=='+':
            return add()
        elif op=='-':
            return sub()
        elif op=='*':
            return mul()
        elif op=='/':
            return div()

numA = 3
numB = 4
op = 'a'
while op != 'q':
    op = raw_input("input the operation: ")
    op_type = operation_factory.get_operation(op)
    op_type.numberA = numA
    op_type.numberB = numB
    print op_type.get_result()
    print '\n'
