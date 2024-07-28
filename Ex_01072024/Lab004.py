#Multiple Inheritance

#Multi Level

class Father:
    key = '123@3456'
    def Father_Method(self):
        print('Father Method')


class Mother:

    def Mother_Method(self):
        print('Mother Method')


class Child(Father,Mother):

    def Child_Method(self):
        print('Child Method')


child = Child()
child.Father_Method()
child.Mother_Method()
child.Child_Method()
print(child.key)