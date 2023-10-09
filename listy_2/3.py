oceny = []
while True: 
    inp = input()
    if inp == "stop":
        break
    inp = float(inp)
    if inp >= 1 and inp <= 6:
        oceny.append(inp)
    else:
        print("podałeś złe liczby Nobie!")
print(oceny)
print(sum(oceny)/len(oceny))
