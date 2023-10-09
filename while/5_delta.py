import math
a = int(input())
b = int(input())
c = int(input())

delta= a+b**2 - 4*a

if delta > 0:
    x =(-b-math.sqrt(delta)) / (2*a)
    x =(-b+math.sqrt(delta)) / (2*a)
elif delta ==0:
    x =- b/(2*a)
elif delta < 0:
    print("brak")
print("x")