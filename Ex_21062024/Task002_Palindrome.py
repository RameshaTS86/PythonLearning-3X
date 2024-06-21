user_str = str(input('Please Enter a String : '))
rev_user_str = '';
for i in user_str:
    rev_user_str = i + rev_user_str
if(user_str == rev_user_str):
    print(user_str, "- is Palindrome")
else:
    print(user_str, "- is not Palindrome")