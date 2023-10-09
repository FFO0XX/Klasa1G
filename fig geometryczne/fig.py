from math import pi 
from math import sqrt

print("SZ = szescan")
print("P = prostopadłościan")
print("W = Walec")
print("S = storzek")
print("K = kula")

a = str(input())

if a == "SZ":
    print("podaj wymiary sześcianu")
    print("a = ")
    a = float(input())
    x = ((6*a)**2)
    y = (a**3)
    print("pole powierzchni szescianu wynosi " + str(x))
    print("obientosc szescianu wynosi "+ str(y))

if a == "P":
    print("podaj wymiary prostopadłoscianu")
    print("a = ")
    a = float(input())
    print("b = ")
    b = float(input())
    print("c = ")
    c = float(input())
    x = (2*(a*b)+2*(a*c)+2*(b*c))
    y = (a*b*c)
    print("pole powierzchni prostopadłoscianu wynosi " + str(x))
    print("obientosc prostopadłoscianu wynosi "+ str(y))

if a == "W":
    print("podaj wymiary walca")
    print("H = ")
    a = float(input())
    print("r = ")
    b = float(input())
    x = (2*(pi*b**2)+2*(pi*a*b))
    y = (pi*a**2*b)
    print("pole powierzchni walca wynosi " + str(x))
    print("obientosc walca wynosi "+ str(y))

if a == "K":
    print("podaj wymiary kuli")
    print("r = ")
    r = float(input())
    x = (4*(pi*r**2))
    y = ((4/3)*(pi*r**3))
    print("pole powierzchni kuli wynosi " + str(x))
    print("obientosc kuli wynosi "+ str(y))

     


