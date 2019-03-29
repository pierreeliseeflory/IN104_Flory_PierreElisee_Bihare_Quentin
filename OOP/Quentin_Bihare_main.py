import animal as Animals
import random as rd


def create_fish_biotope(n):
    biotope=[]
    for i in range(n):
        k=rd.randint(0,2)   
        if k == 0 :
            blue_fish=Animals.Fish("blue",0.1,0.5,0.5,1,0.1,True)
            biotope.append(blue_fish)
        elif k == 1 :
            red_fish=Animals.Fish("red",0.1,0.5,0.5,1,0.1,True)
            biotope.append(red_fish)
        else :
            yellow_fish=Animals.Fish("yellow",0.1,0.5,0.5,1,0.1,True)
            biotope.append(yellow_fish)
    return biotope

def create_feline_biotope(n):
    biotope=[]
    for i in range(n):
        k=rd.randint(0,2)   
        if k == 0 :
            cat=Animals.Feline(10,False,True,3,3,1,0.2,True)
            biotope.append(cat)
        elif k == 1 :
            panther=Animals.Feline(70,False,True,0.5,0.5,0.2,0.5,True)
            biotope.append(panther)
        else :
            lion=Animals.Feline(60,False,True,0.5,0.5,0.2,0.3,True)
            biotope.append(lion)
    return biotope


def main():

    biotope=create_fish_biotope(4)
    colors=[]
    fish_hunger=[]
    for fish in biotope:
        color=fish.get_color()
        colors.append(color)
        fish.tic()
        fish.tic()
        fish.eat()
        hunger=fish.get_hunger_bar()
        fish_hunger.append(hunger)
    for i in range(4):
        print("I'm a",colors[i],"fish","My hunger rate is ",fish_hunger[i]*100,"% atm")

    biotope2=create_feline_biotope(3)
    speeds=[]
    hunting =[]
    awake = []
    for feline in biotope2:
        speed=feline.get_speed()
        speeds.append(speed)
        feline.go_on_hunt()
        awake.append(not(feline.sleeping))
        hunting.append(feline.get_on_hunt())

    for i in range(3):
        print("I run at",speeds[i],"mph.","Am I on a hunt?",hunting[i],"Am I sleeping?",awake[i])
        

main()
