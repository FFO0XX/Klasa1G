from random import*

def random_oponent():
    opponents = [
        ["poison bee", 6, 2, 50],
        ["poison bee", 6, 2, 50],
        ["poison bee", 6, 2, 50],
        ["earth worm", 20, 10, 100],
        ["earth worm", 20, 10, 100],
        ["GOBLIN",30 ,10, 300 ]
    ]
    return choice(opponents)

def Dragon_Attacks():
    attacks = [
        ["dragon_breath",20,0,0],
        ["bite",15,0,0],
        ["bite",15,0,0],
        ["claw slash",10,0,0],
        ["claw slash",10,0,0],
        ["claw slash",10,0,0],
        ["claw slash",10,0,0]
    ]
    return choice(attacks)