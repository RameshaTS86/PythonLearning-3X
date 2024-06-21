user_str1 = str(input('Please Enter a String 1 : ')).lower()
user_str2 = str(input('Please Enter a String 2 : ')).lower()

if(len(user_str1)==len(user_str2)):
    list_str1 = list(user_str1)
    list_str2 = list(user_str2)
    list_str1.sort()
    list_str2.sort()
    if(list_str1 == list_str2):
        print('Entered Strings are Anagram Strings')
    else:
        print('Entered Strings are not Anagram Strings')

else:
    print('Entered Strings are not Anagram Strings')