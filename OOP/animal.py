class Animals:
    def __init__(self, size, weight, hunger_bar, hunger_decrease_rate, alive):
        self.size = size
        self.weight = weight
        self.hunger_bar = hunger_bar
        self.hunger_decrease_rate = hunger_decrease_rate
        self.alive = True

    def tic(self):
        self.hunger_bar -= self.hunger_decrease_rate

    def get_hunger_bar(self):
        return self.hunger_bar

# Add death marks and create a main in which you create the biotope


class Fish(Animals):
    def __init__(self, color, eating_speed, size, weight, hunger_bar, hunger_decrease_rate, alive):
        Animals.__init__(self, size, weight, hunger_bar,
                         hunger_decrease_rate, alive)
        self.color = color
        self.eating_speed = 0.1

    def get_color(self):
        return self.color

    def get_eating_speed(self):
        return self.eating_speed

    def eat(self):
        if self.hunger_bar < 1:
            self.hunger_bar += self.eating_speed


class Feline(Animals):
    def __init__(self, speed, on_hunt, sleeping, size, weight, hunger_bar, hunger_decrease_rate, alive):
        Animals.__init__(self, size, weight, hunger_bar,
                         hunger_decrease_rate, alive)
        self.speed = speed
        self.sleeping = sleeping
        self.on_hunt = on_hunt

    def get_speed(self):
        return self.speed

    def get_on_hunt(self):
        return self.on_hunt

    def get_sleeping(self):
        return self.sleeping

    def wake_up(self):
        self.sleeping = False

    def go_on_hunt(self):
        if self.hunger_bar <= 0.3:
            self.wake_up()
            self.on_hunt = True

    def sleep(self):
        if hunger_bar > 1:
            self.on_hunt = False
            self.sleeping = True
