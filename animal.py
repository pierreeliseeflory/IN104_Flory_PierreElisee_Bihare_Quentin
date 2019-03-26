class Animals : 
    def __init__(self,size,weight,hunger_bar,hunger_decrease_rate,alive):
        self.size = size
        self.weight = weight
        self.hunger_bar = hunger_bar
        self.hunger_decrease_rate = hunger_decrease_rate
        self.alive = True
    
    def tic(self):
        self.hunger_bar -= self.hunger_decrease_rate
        

class Fish(Animal) :
    def __init__(self,color,eating_speed):
        self.color = color
        self.eating_speed = 0.1 

    def get_color(self):
        return self.color

    def get_eating_speed(self):
        return self.eating_speed

    def eat(self):
        if self.hunger_bar < 1 :
            self.hunger_bar += self.eating_speed

class Feline(Animal):
    def __init__(self,speed,on_hunt,sleeping, awake):
        self.speed = speed
        self.awake = True
        
    def get_speed(self):
        return self.speed

    def go_on_hunt(self)
        if self.hunger_bar < 0.3 :
            self.on_hunt = True

    def wake_up(self):
        self.awake = True
    
    def eat(self):
        if self.on_hunt==True and 
    
    def sleep(self):
        if hunger_bar > 1:
            self.on_hunt = False
            self.sleeping = True 
        