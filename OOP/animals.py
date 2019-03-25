class Animals:
    def __init__(self, age, weight, alive):
        self.age = age
        self.weight = weight
        self.alive = alive


def Insects(Animals):
    def __init__(self, longevity, initialSpeed):
        self.longevity = longevity
        self.initialSpeed = initialSpeed

    def getNumberOfLegs(self):
        return 6

    def getSPeed(self):
        return self.age * self.initialSpeed

    def death(self):
        self.alive = false


def Birds(Animals):
    def __init__(self, canFly, needsToEat):
        self.canFly = canFly
        self.needsToEat = needsToEat

    def getSpeed(self):
        if self.canFly:
            if self.weight > 10:
                return 5
            elif self.weight > 5:
                return 10
            return 20
        return 1

    def eat(self)
    return self.needsToEat = false
