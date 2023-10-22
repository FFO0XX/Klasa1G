x = str(input("podaj słowo: "))
z = ""
for y in x:
    z = y + z
if z == x:
    print("słowo jest palindromem")
else:
    print("słowo nie jest palindromem")