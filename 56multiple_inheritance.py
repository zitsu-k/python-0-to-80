# multiple inheritance = when a child class is derived from more than one parent class
class Prey:
    def flee(self):
        print("this animal flees")

class Predator:
    def hunt(self):
        print("this animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.flee()
fish.hunt()































