num = int(input('Please Enter a Number : '))
first_num = 0
second_num = 1
next_num = first_num
count = 1
while(count <=num):
    print(next_num,end=" ")
    first_num = second_num
    second_num = next_num
    next_num = first_num + second_num
    count +=1