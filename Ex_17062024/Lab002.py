def f1(a,b,c):
    return a+b+c
    #print("Addition Done") -- #After return no code will get execute


result=f1(1,2,3)
print(result)
result1=f1(a=3,b=8,c=9)
print(result1)

result1=f1(c=3,a=8,b=9)
print(result1)

result1=f1(c=1,a=2,b=3)
print(result1)
