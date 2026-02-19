class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

class Pet(Animal):
    def barks(self):
        print(self.name, "barks")


d = Dog("Buddy")
p = Pet("Tiger")
d.info()      # Inherited method
d.sound()
p.info()
p.barks()
