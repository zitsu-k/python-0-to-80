#multi-level inheritance = when a derived class (child ) class inherits another derived 

class Organism:

    alive = True
class Animal(Organism):
    def eat(self):
        print("this animal is eating ")

class Dog(Animal):
    def bark(self):
        print("the dog is barking ")
dog = Dog()

print(dog.alive)
dog.eat()
dog.bark()





