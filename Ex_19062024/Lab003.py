#Lambda Exmaples


def odd_even(n):
    if(n%2==0):
        print('Even')
    else:
        print('Odd')

result=odd_even((2))

#in lAmbda

odd_even = lambda  num : 'Even' if num%2==0 else 'Odd'
print(odd_even(0))



def double_sal(salary):
    return salary* 2

result=double_sal((20000))
print(result)
#in lAmbda

l_ds = lambda  salary : salary *2
print('Lambda Salary : ',l_ds(50000))