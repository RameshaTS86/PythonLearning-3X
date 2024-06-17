def say_hello(): #No Return and No Parameter
    print("Hello")

say_hello()

def say_heelo_to_someone(name ='Ramesh'): #No Return and 1 Parameter
    print('Hello ',name)

say_heelo_to_someone()
say_heelo_to_someone('Vignesh')
say_heelo_to_someone(name = 'Bhoomika')

#Argument and Parameter

def add_two_num(num1,num2):
    return num1+num2

print(add_two_num(12,12))

#Default Argument and Parameter

def add_two_num(num1= 10,num2=10):
    return num1+num2

print(add_two_num())
print(add_two_num(12,45))