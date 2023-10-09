print("podaj wymiary trójkąta")

a = float(input())
b = float(input())
c = float(input())

if a + b > c and b + c > a and a + c > b:
    print("jest to trujkąt")
else:
    print("nie jest to trójkąt")