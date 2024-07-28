#Multiple Inheritance

#Method Resolution

class Father:
    key = '123@3456'
    def Father_Method(self):
        print('Father Method')

    def Method1(self):
        print('Father Method')


class Mother:

    def Mother_Method(self):
        print('Mother Method')

    def Method1(self):
        print('Mother Method')

class Child(Mother,Father):

    def Child_Method(self):
        print('Child Method')




child = Child()
child.Father_Method()
child.Mother_Method()
child.Child_Method()
child.Method1()  #Method Resolution Order
print(child.key)