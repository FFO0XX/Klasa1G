
import uuid  
# inf list

def informacje(lista:list)->None:
    for slownik in lista:
        for k,v in slownik.items():
            print(f"{k}:   {v}")
        print("==="*20)
# + ksiąrzki do listy

def dodaj_ksiazke(lista):
    x = input("podaj tytuł")
    y = input("podaj liczbe stron")
    z = input("podaj autora")
    ksiazka = {
        'nazwa': x,
        'ilość stron': y,
        'autor': z,
        'id': uuid.uuid4()
    }
    lista.append(ksiazka)
#- słowniki z listy

def istnieje(lst: list, id: str):
    for i in range(len(lst)):
        if str(lst[i]["id"]) == id:
            return True
    return False

def index(lista: list, id: str):
    for i in range(len(lista)):
        if str(lista[i]["id"]) == id:
            return i
    return -1  

def usun(lista: list) -> None:
    inp = input("Podaj id książki: ")
    if istnieje(lista, inp):
        index = index(lista, inp)
        if index != -1:
            lista.pop(index)
            print("Ksiażka usunięta")
        else:
            print("Nie ma takiej książki")
    else:
        print("Nie ma takiej książki")
#edit dane słowniki

def edytowanie(lista:list):
    x = input("Którą książkę chcesz edytować?(podaj id)")
    if istnieje(lista, x):
        idd = index(lista, x)
        z = input("Co chcesz edytować?")
        lista[idd][z] = input("wprwadź dane ")
        print(lista[idd][z])
