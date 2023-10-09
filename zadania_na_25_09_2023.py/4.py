lista = [0,1,2,3,4,5,6,7,8,9]

print("podaj dowolną liczbe")
a = int(input())

if a in lista:
    print(str(a) + " jest w liście")
else:
    print(str(a) + " nie jest w liście")