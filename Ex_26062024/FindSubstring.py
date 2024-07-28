sub_str = str(input('Please Enter a Sub String : '))
main_str = 'India has 30 states and 8 union territories and it is a democratic country'

if sub_str.lower() in main_str.lower():
    print('Substring found',sub_str)
else:
    print('Substring not found', sub_str)