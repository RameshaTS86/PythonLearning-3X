user_str = str(input('Please Enter a String to Reverse : '))

#Using string slice method
print('Reverse String using string slice method [::-1] : ',user_str[::-1])

#Using For Loop
rev_str =''
for i in user_str:
    rev_str = i+rev_str
print('Reverse String Using for loop : ', rev_str)

#using List
user_str_list = list(user_str)
user_str_list.reverse()
rev_str1 = ''
for i in user_str_list:
    rev_str1 += i
print('Reverse String using list : ', rev_str1)


