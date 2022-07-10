from math import sqrt
print("""Program to calculate the area of a triangle
using 3 inputs from the user""")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
s = (a + b + c) / 2
area = sqrt(s * (s-a) * (s-b) * (s-c))

print("The area of the triangle is:", area)
