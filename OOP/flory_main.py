import animals as Animals


def ant_creation(name):
    tmp = Animals.Insects(10, 2)
    tmp.age = 0
    tmp.weight = 1
    tmp.alive = True
    tmp.name = name
    return tmp


def bird_creation(canFly, needsToEat, weight, maxAge, name):
    tmp = Animals.Birds(canFly, needsToEat, maxAge)
    tmp.age = 0
    tmp.weight = weight
    tmp.alive = True
    tmp.name = name
    return tmp


def main():
    ant1 = ant_creation("ant1")
    ant2 = ant_creation("ant2")
    pigeon = bird_creation(True, 0, 2, 15, "pigeon")
    ostrich = bird_creation(False, 0, 50, 30, "ostrich")
    predators = [pigeon, ostrich]
    preys = [ant1, ant2]
    animals = [pigeon, ostrich, ant1, ant2]
    for day in range(0, 20):
        print("Jour n°", day, " :")
        for predator in predators:
            for prey in preys:
                if predator.needsToEat > 3 and predator.alive:
                    if prey.alive:
                        predator.eat(prey)
                        prey.death(True, predator)
                        if not prey.alive:
                            print(predator.name, " a mangé ", prey.name)
        for animal in animals:
            if animal.alive:
                animal.birthday()
        for prey in preys:
            if prey.alive:
                prey.death(False, None)
                if not prey.alive :
                    print(prey.name, " est mort de vieillesse")
        for predator in predators:
            if predator.alive:
                predator.needsToEat += 1
                predator.death()
                if not predator.alive :
                    print(predator.name, " est mort de vieillesse ou de faim")
main()
