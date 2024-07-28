#Inheritance - Acquire the Attribute and Behaviour ex Data Member and  Data Method
#types of Inheritance
#1. Single Inheritance
#2. Multiple Inheritance
#3. MultiLevel Inheritance
#4. Hierarchical Inheritance
#5. Hybrid Inheritance
class GrandFather:
    key = '123@3456'
    def GrandFather_Method(self):
        print('Grand Father Method')


class Father(GrandFather):

    def Father_Method(self):
        print('Father Method')

fat = Father()
fat.GrandFather_Method()
fat.Father_Method()
print(fat.key)