a = int(input("podaj ocenę szkolną"))

if a <= 0 or a >=7:
    print("nie jest to ocena szkolna")
elif a >= 4 :
    print("zaliczone")
else:
    print("niezalicznone")