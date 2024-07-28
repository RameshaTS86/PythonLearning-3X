#Handling with Exception
print('Start of the Program')
print('-----------------------------')
try:
    a = int(input('Please Enter a Number1 : '))
    b = int(input('Please Enter a Number2 : '))
    c = a / b
    print('Result Div is : ', c)
except Exception as e:
    print('Error : ',e)
print('-----------------------------')
print('End of the Program')
