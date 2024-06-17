def sum_args(a,b,*args):  #args will store the values in list [4,6]
    sum=0
    for i in args:
        sum += i
    return sum+a+b

print(sum_args(1,2,4,6,4,6,4,6))