#Inheritance


#Parent Class



class ParentClass:
    P_A01= 1000
    _P_A02= 200
    __P_A03= 300

    def parent_method(self):
        print('I am Parent Class Public Method')

    def _parent_method2(self):
        print('I am Parent Class Protected Method')

    def _parent_method3(self):
        print('I am Parent Class Private Method')


class Parent2:
    P2_A01=10000

    def Parent2(self):
        print('I am Parent 2')

#ChildClass

class Child(ParentClass,Parent2):
    pass


#SuperChild

class SuperChild(Child):
    pass





cc = Child()
print(cc.P_A01)
cc.parent_method()
cc.Parent2()

sc = SuperChild()

