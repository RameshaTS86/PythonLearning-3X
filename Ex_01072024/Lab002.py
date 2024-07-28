class Parent:
    gold = '2kg'

    def Home_2bhk(self):
        print('Parent - 2BHK')

class Child1(Parent):
    def Home_3bhk(self):
        print('Child1 - Parent')

class Child2(Parent):
    def Home_3bhk(self):
        print('Child2 - Parent')
class Child3(Parent):
    def Home_3bhk(self):
        print('Child3 - Parent')

child = Child1()
print(child.gold)
child.Home_2bhk()
child.Home_3bhk()
print('---------------------------------------------------')
child = Child2()
print(child.gold)
child.Home_2bhk()
child.Home_3bhk()
print('---------------------------------------------------')
child = Child3()
print(child.gold)
child.Home_2bhk()
child.Home_3bhk()