#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).

side1 = int(input('Please Enter Length of Side1 : '))
side2 = int(input('Please Enter Length of Side2 : '))
side3 = int(input('Please Enter Length of Side3 : '))

if(side1 ==side2 and side2==side3):
    print("Equilateral")
elif((side1==side2 and side2 != side3) or(side1==side3 and side3!=side2) or (side2==side3 and side2!=side1)):
    print("Isosceles")
else:
    print("Scalene")