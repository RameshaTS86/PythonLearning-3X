user_str = str(input('Please Enter a String : '))
vowels = ['a','e','i','o','u']
user_str = user_str.lower()
vowel_count = 0
consonenet_count = 0

for i in user_str:
    if i in vowels:
        vowel_count += 1
    else:
        consonenet_count += 1
print('Vowel Count : ',vowel_count)
print('Consonent Count : ',consonenet_count)