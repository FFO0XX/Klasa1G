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

duplicates = []
while True:
    for i in range(len(numbers)):
        if numbers[i] == numbers[0] or numbers[1] or numbers[2] or numbers[3] or numbers[4]:
            duplicates.append(numbers[i])
            print(duplicates)
            numbers.remove(numbers[i])
            print(numbers)
    break

for i in range(len(numbers)):
    print(numbers[i]**2)