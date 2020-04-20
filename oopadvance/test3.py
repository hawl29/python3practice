class Animal(object):
    pass
class Mammal(Animal):
    pass
class Brid(Animal):
    pass
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Ostrich(Brid):
    pass
class Parrot(Brid):
    pass

class Runnable(object):
    def run(self):
        print("Running...")

class Flyable(object):
    def fly(self):
        print("Flying")

class Dog(Mammal,Runnable):
    pass

d = Dog()
d.run()