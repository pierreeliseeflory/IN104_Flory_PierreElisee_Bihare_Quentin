class Animals:
    def __init__(self, age, weight, alive, name):
        self.age = age
        self.weight = weight
        self.alive = alive
        self.name = name

    def birthday(self):
        self.age += 1


class Insects(Animals):
    def __init__(self, longevity, initialSpeed):
        self.longevity = longevity
        self.initialSpeed = initialSpeed

    def getNumberOfLegs(self):
        return 6

    def getSpeed(self):
        return self.age * self.initialSpeed

    def death(self, attacked, attacker):
        if self.age > self.longevity:
            self.alive = False
        elif attacked:
            if self.getSpeed() < attacker.getSpeed():
                self.alive = False


class Birds(Animals):
    def __init__(self, canFly, needsToEat, maxAge):
        self.canFly = canFly
        self.needsToEat = needsToEat
        self.maxAge = maxAge

    def getSpeed(self):
        if self.canFly:
            if self.weight > 10:
                return 5
            elif self.weight > 5:
                return 10
            return 50
        return 1

    def eat(self, attacked):
        if self.getSpeed() > attacked.getSpeed():
            self.needsToEat = 0

    def death(self) :
        if self.age > self.maxAge or self.needsToEat > 10 :
            self.alive = False
