#SET

my_set1 ={1,2,3,3,4,5,6,6,7}
print(my_set1)
print(len(my_set1))

myset2 = {1,2,3,8,9}
print(myset2)


#union
union_set1 = my_set1.union(myset2)
print(union_set1)

#Intersection
union_set1 = my_set1.intersection(myset2)
print(union_set1)

#Difference
union_set1 = my_set1.difference(myset2)
print(union_set1)

#Difference
union_set1 = myset2.difference(my_set1)
print(union_set1)

ssubset={1,2,3}

print(ssubset.issubset(my_set1))

my_set1.add(100)
print(my_set1)

my_set1.pop()
print(my_set1)