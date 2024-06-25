#Recursiion

# /-div
# // - Quotient
# % Reminder

def sum_of_digit(num):
    if num <10:
        return num
    else:
        return num%10 + sum_of_digit(num//10)


def sum_of_digits(num):
    sum_of_digi = 0
    while(num > 0):
        sum_of_digi += num %10
        num = num // 10
    return sum_of_digi

print(sum_of_digits(123459))