#Factorial

number = int(input("Please Enter a Number to Calculate Factorial : "))

if(number<0):
    print("Invalid Number")
else:
    fact = 1
    if(number == 0):
        fact = 1
    else:
        for i in range(0,number):
            fact = fact * (number-i)
    print(fact)



