x = 0

numbers = []
while True:
    if len(numbers) < 5:
        a = int(input("podaj liczbę do listy: "))
        numbers.append(a)
    else:
        break
print("suma listy numbers to " + str(sum(numbers)))

for i in range(len(numbers)):
    if (numbers[i]) > int(x):
        x = numbers[i]
print("największa liczba w liście numbers to " + str(x))

x = numbers[0]

for i in range(len(numbers)):
    if (numbers[i]) < int(x):
        x = numbers[i]
print("najmniejsza  liczba w liście numbers to " + str(x))
print("średnia arytmetyczna listy numbers to " + str(sum(numbers)/len(numbers)))

z = 0
for i in range (len(numbers)):
    if numbers[i] % 2 == 0:
        z+=1
print("liczba parzystych liczb wynosi " + str(z))



#8 i 9 skopiowałem z rozwiązań bo nie wiedziałem jak to zrobić samemu a potrzebowałem do kolejnych podpunktów
duplicates = []

while True:
    for i in range(len(numbers)):
        if numbers.count(numbers[i]) > 1 and numbers[i] not in duplicates:
            duplicates.append(numbers[i])
    break
print("duplikaty w numbers to "+ str(duplicates))

new_list = []

i = 0
while True:
    for i in range(len(numbers)):
        if numbers[i] not in new_list:
            new_list.append(numbers[i])
    break
numbers = new_list



squares = []
for i in range(len(numbers)):
    squares.append((numbers[i]**2))
print("kwadraty 'numbers' to " +  str(squares))


numbers.reverse()
print(numbers)

liczba = input("podaj liczbę: ")

i = 0
while  i < len(numbers):
    if int(numbers[i]) == int(liczba) and i < len(numbers):
        print(str(liczba) + " występuje na miejscu " + str(i))
        i+=1
    elif i >= len(numbers):
        break
    else:
        i+=1
liczba_wienksz = 0
for i in range(len(numbers)):
    if numbers[i] > 10:
        liczba_wienksz += 1
print("w numbers jest " + str(liczba_wienksz) + " liczb większych od 10")


numbers.sort

print("numbers od największej do najmniejszej to " + str(numbers))


najw = 0
praw_najw = 0
for i in range(len(numbers)):
    if int(numbers[i]) > najw:
        praw_najw = najw
        najw = numbers[i]
    elif int(numbers[i]) > praw_najw and numbers[i] != najw:
        praw_najw = numbers[i]
print("prawie najwiękasza liczba w numbers to " + str(praw_najw)) 

doubled_numbres = []

for i in range(len(numbers)):
    doubled_numbres.append(int(numbers[i])*2)
print("podwojone wartości każdej liczby z numbers to " + str(doubled_numbres))

numbers = []
while True:
    if len(numbers) < 5:
        a = int(input("podaj liczbę do listy: "))
        numbers.append(a)
    else:
        break
print("suma listy numbers to " + str(sum(numbers)))

for i in range(len(numbers)):
    x = numbers.count(numbers[i])
    print("w numbers jest " +  str(x) + " liczby " + str(numbers[i]))

for i in range(len(numbers)):
    print(str(numbers[i]) + " ma index " + str(i))


    
