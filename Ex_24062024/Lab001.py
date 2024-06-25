#Filters

List1= [1,2,3,4,5,6,7,8,9,10]

def is_evn(num):
    return num%2==0

even_ls = list(filter(is_evn,List1))
print(even_ls)