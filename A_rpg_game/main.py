from random import*
from enemies import*

#=======================================
print("what is your name traveler?")
name = str(input())

manacap = 100
mana = 100
hp = 100
stamina = 100
G = 0
maxsdmg = 20
maxfdmg = 30
sword_dmg = randint(1,maxsdmg)
fireball_dmg = randint(10,maxfdmg)


#==============Ataccks==================

def attack_method():
    print("A/a - fireball")
    print("B/b - Sword slash")
    inp = input()
    if inp.upper() == "A":
        print("FIREBALL")
        return fireball()
    if inp.upper() == "B":
        print("HAJJJJJJJJJJJJJA")
        return sword_slash()

def fireball():
    global mana
    if mana <= 5:
        print("you dont have any mana left")
        return 0
    else:
        mana -=10
        print(f"you now have {mana} mana")
        return fireball_dmg
        

def sword_slash():
    global stamina
    if stamina < 5:
        print("you dont have any stamina left")
        return 0
    else:
        stamina -= 5
        print(f"you have {stamina} stamina left")
        return sword_dmg
#==================other def"s"=============
def forest():
    global hp
    global G
    print("=============ENTERING THE FORREST=============")
    poisoned = False
    enemie_number = 0
    enemie_togo = 5
    while enemie_number < 5:
        enemie = random_oponent()
        print(f"{enemie[0]}  appered! press K to chose an attack method")
        inp = str(input())
        if inp.upper() == "K":
            while enemie[1] > 0:
                uratack = attack_method()
                if poisoned == True:
                    hp -= 3 
                    if hp <= 0:
                        print(f"{enemie[0]} killed you")
                        print(f"YOU DIED")
                        exit()
                    print(f"you took 3 poison dmg you now have {hp} hp")
                if enemie[0] == "poison bee":
                    chance_of_success = randint(0,30)
                    if chance_of_success >= 20:
                        enemie[1] -= uratack
                    else:
                        print(f"{enemie[0]} dogged your attack")
                        hp -= enemie[2]
                        if hp <= 0:
                            print(f"{enemie[0]} killed you")
                            print(f"YOU DIED")
                            exit()
                        print(f"{enemie[0]} attacked you and dealt {enemie[2]} hp, you now have {hp} hp")
                        print(f"{enemie[0]} infected you with poison you will now take 3 poison dmg every move until you kill all 5 monsters")
                        poisoned = True
                        print(f"poison bee still has {enemie[1]} hp")
                        break
                else:
                    enemie[1] -= int(uratack)
                if enemie[1] <= 0:
                    enemie_togo -= 1 
                    print(f"{enemie[0]} died({enemie_togo} left)")
                    G += enemie[3]
                    print(f"you gained {enemie[3]} gold you now have {G} gold")
                    enemie_number += 1
                    break
                else:
                    print(f"you dealt {uratack} dmg and {enemie[0]} now has {enemie[1]} hp")
                    hp -= enemie[2]
                    if hp <= 0:
                        print(f"{enemie[0]} killed you")
                        print(f"YOU DIED")
                        exit()
                    print(f"he attacked you and dealt {enemie[2]} hp, you now have {hp} hp")
    print("CONGRATULATIONS YOU KILLED ALL 5 BASIC ENEMIES, YOU CAN NOW COME BACK TO THE VILLAGE")
    print("if you wish to come back to the village press K")
    inp = str(input())
    if inp.upper() == "K":
        print("==============TRAVELLING TO VILLAGE==============")
    else:
        print(f"A ogre Ambushed and killed you(bc you didn't press 'k' you pressed {inp}")
        print(f"YOU DIED")
        exit()
    print(f"{name} YOU CAME BACK FORM THE FOREST! {name} I will reward you with 1500G.")
    G += 1500
    print(f"you now have {G} gold")
    stamina = 100
    mana = manacap
    print(f"your mana and stamina will be automaticly refiled after you go back from the forest")
    print(f"you now have {mana} mana and {stamina} stamina")
#village npc
def Bob():
    print(f"hello {name} You can visit:")
    print(f"the 'Alchemist' to refill your mana or/and hp, ")
    print(f"the 'SwordMaster' to train with the sword and increase your sword slash damage,")
    print(f"the 'Arcane Wizard' to train with your magic proficency and increase your fireball damage,")
    print(f"You can also go back to the forest and get more gold,")
    print(f"ORRRRRRR you can go and deafeat the: 'MIGHTY DRAGON OF ALL REVINES AND MOUNTAINS'(but he is strong)")
    print(f"press q/Q to visit the 'Alchemist'")
    print(f"press w/W to visit the 'SwordMaster'")
    print(f"press e/E to visit the 'Arcane Wizard'")
    print(f"write 'GO BACK I WANT TO BE MONKE' to go back to the forest")
    print(f"write 'kill drogoon' to go and fight the 'MIGHTY DRAGON OF ALL REVINES AND MOUNTAINS'")
    inp = input()
    if inp.upper() == "Q":
        Travel_Alchemist()
    elif inp.upper() == "W":
        Travel_SwordMaster()
    elif inp.upper() == "E":
        Travel_Arcane_Wizard()
    elif inp.upper() == "GO BACK I WANT TO BE MONKE":
        Travel_Forest()
        Bob()
    elif inp.upper() == 'KILL DROGOON':
        Travel_Dragoon()
#alchemist
def Travel_Alchemist():
    print("what can i do for you?")
    print("press a/A to refill hp for 500G")
    print("press c/C to refill stamina for 500G")
    print("write 'goback' to go back to Bob")
    inp = input()
    if inp.upper() == "A" and G >= 500:
        REF_HEALTH()
        print(f"you now have {hp} hp and {G} gold")
        Travel_Alchemist()
    elif inp.upper() != "C" and inp.upper() != "GOBACK" :
        print("ya dont have enough money pal(or you pressed the wrong key :D)")
        Travel_Alchemist()
    elif inp.upper() == "C" and G >= 500:
        REF_STAMINA()
        print(f"you now have {stamina} stamina and {G} gold")
        Travel_Alchemist()
    elif inp.upper() != "A" and inp.upper() != "GOBACK":
        print("ya dont have enough money pal(or you pressed the wrong key :D)")
        Travel_Alchemist()
    elif inp.upper() == "GOBACK":
        Bob()
def REF_HEALTH():
    global G
    global hp 
    hp = 100
    G -=500
def REF_MANA():
    global G
    global mana 
    mana = 100
    G -=500
def REF_STAMINA():
    global G
    global stamina 
    stamina = 100
    G -=500
#SwordMaster

def Travel_SwordMaster():
    global G
    global maxsdmg
    print("what can i do for you?")
    print("press a/A to train for 1000G(increase sword dmg)")
    print("write 'goback' to go back to Bob")
    inp = str(input())
    if inp.upper() == "A" and G >= 1000:
        maxsdmg += 10
        G -=1000
        print(f"your swordslash now can deal up to {maxsdmg} damage")
        print(f"you now have {G} gold")
        Travel_SwordMaster()
    elif inp.upper() == "GOBACK":
        Bob()

#Arcane Wizard
def Travel_Arcane_Wizard():
    global G
    global manacap
    global mana
    global maxfdmg
    print("what can i do for you?")
    print("press a/A to train for 1000G(increase fireball dmg and mana capacity)")
    print("write 'goback' to go back to Bob")
    inp = str(input())
    if inp.upper() == "A" :
        maxfdmg+= 10
        manacap +=50
        mana = manacap
        G -= 1000
        print(f"your fireball now can deal up to {maxfdmg} damage and have a max mana pool of {manacap}")
        print(f"you now have {G} gold")
        Travel_Arcane_Wizard()
    elif inp.upper() == "GOBACK":
        Bob()

#TRAVEL FORREST
def Travel_Forest():
    print("good luck!")
    forest()

#Travel dragoon
def Travel_Dragoon():
    print(f"WWWWWWWWWWWWWWWWWW=TRAVELING TO DRAGONS LAIAR=WWWWWWWWWWWWWW")
    print("arrived")
    dragonfight()
#dragon fight
def dragonfight():
    global G
    global hp
    global stamina
    dragon_hp = 300
    print(f"{name} you -insert f-word here + ing- HUMAN YOU HAVE ARRIVED IN MY LAIAR WILL YOU PICK A FIGHT WITH ME OR ARE YOU GONA RUN AWAY?!?!?!?!?!!?")
    print("press K to fight")
    print("press R to run away")
    inp = input()
    if inp.upper() == "R":
        print("running away...")
        print("========TRAVELING TO VILLAGE========")
        Bob()
    elif inp.upper() == "K":
        while dragon_hp > 0:
            print("choose an attack method")
            joratak = attack_method()
            chance_of_crit = randint(0,10)
            chance_dragon_hit = randint (0,100)
            if chance_of_crit >= 7:
                dragon_hp -= (joratak*2)
                print("CRIT")
                if dragon_hp <= 0 :
                    print("YOU MANAGED TO DEAFEAT THE:'MIGHTY DRAGON OF ALL REVINES AND MOUNTAINS'(gratki)")
                    break
                print(f"you hit the dragon for {joratak*2} dmg he now has {dragon_hp} hp ")
            else:
                dragon_hp -= joratak
                if dragon_hp <= 0 :
                    print("YOU MANAGED TO DEAFEAT THE:'MIGHTY DRAGON OF ALL REVINES AND MOUNTAINS'(gratki)")
                    break
                print(f"you hit the dragon for {joratak} dmg he now has {dragon_hp} hp ")
            if chance_dragon_hit > 45:
                dragatack = Dragon_Attacks()
                print(f"The dragon managed to hit you with {dragatack[0]} for {dragatack[1]} dmg ")
                hp -= dragatack[1]
                if hp <= 0:
                    print(f"'MIGHTY DRAGON OF ALL REVINES AND MOUNTAINS' killed you")
                    print(f"YOU DIED")
                    exit()
                print(f"You now have {hp} hp")
            else:
                if hp <= 90:
                    hp+=10
                if stamina <= 95:
                    stamina += 5
                print(f"you DOGED, you managed to rest and recover 10 hp and 5 stamina you now have {hp} hp and {stamina} stamina")
    print("THE: 'MIGHTY DRAGON OF ALL REVINES AND MOUNTAINS' dropped an 'god fragment' your hp will rise 10x your proficency in fireball will be maxed also you will gain 99999999 gold ")
    
    maxsdmg = 999
    maxfdmg = 999
    hp = 999
    G += 99999999
    print(f"you now have {hp} hp, deal up to {maxfdmg} wit the sword and fireball and have {G} gold")
    Bob_THE_GOD_OF_ALL()
def Bob_THE_GOD_OF_ALL():
    print("==============TRAVELING TO VILLAGE=============")
    print("Bob:")
    print(f"hello {name} you managed to kill the 'MIGHTY DRAGON OF ALL REVINES AND MOUNTAINS' congratulations... actualy the thing is... there is another threat it, or should I say")
    print("he is... MEEEEEEEEEEEEEEEE")
    print("I AM BOB THE GOD OF ALL, THE CREATOR OF ALL GALAXYS AND YOU KILLED MY FAVORITE PET YOUR PENALTY WILL BE DEATH")
    print("WOOOOOOSH")
    print("A cucumber stabbed you")
    print("YOU DIED(ty for playing my game)")
    exit()

        
 
#============Phase one==================
inp = "xD"
while inp != 'perhaps':
    print("I will give you a small quest, if you wish to accept it just say 'perhaps'")
    inp = str(input())
    if inp == 'perhaps':
        print(f"{name} you will embark on a jurney to the forest and slay 5 bacic enemies, if you do, I will reward you with a bundle of gold my name is Bob btw")
        break
#============The forest=================
forest()
#===============VILLLAGE
Bob()
