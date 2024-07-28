try:
    a = int(input('Please Enter a Number1 : '))
    b = int(input('Please Enter a Number2 : '))
    c = a / b

except ValueError as e:
    print('Error : ',e)
except ZeroDivisionError as d:
    print('Error : ',d)
else:
    print('Result Div is : ', c)
finally:
    print('I am Final Class')