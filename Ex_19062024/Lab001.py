#Locall Variable

def my_fun():
    a=10 #local Variable
    print('Hello')
    print(a)

#print(a)
my_fun()


#Global Variable

global_var = 20
def my_fun1():
    a=10 #local Variable
    print('Hello')
    print('Global variable : ',global_var)

print(global_var)
my_fun1()