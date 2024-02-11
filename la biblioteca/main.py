
from ksiarzki import*
from definicje import*


while True:
    print("==="*20)
    print("i - informacje")
    print("e - edytuj dane")
    print("d - dodaj ksiazke")
    print("u - usun ksiazke")
    print("==="*20)
    dzialanie = input()
    if "i" == dzialanie:
        informacje(biblioteka)
    elif "e" == dzialanie:
        edytowanie(biblioteka)
    elif "u" == dzialanie:
        usun(biblioteka)
    elif "d" == dzialanie:
        dodaj_ksiazke(biblioteka)