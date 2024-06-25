list_alphabet = ['q','e','a','f','v','i','u','j','x','o','t','d']

def vowels(letter):
    vowels_ls = ['a','e','i','o','u']
    if letter not in vowels_ls:
        return letter


vowel_ls = list(filter(vowels,list_alphabet))
print(vowel_ls)