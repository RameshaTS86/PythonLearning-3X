#Multi Level

class GrandFather:
    key = '123@3456'
    def GrandFather_Method(self):
        print('Grand Father Method')


class Father(GrandFather):

    def Father_Method(self):
        print('Father Method')


class Child(Father):

    def Child_Method(self):
        print('Child Method')


child = Child()
child.GrandFather_Method()
child.Father_Method()
child.Child_Method()
print(child.key)