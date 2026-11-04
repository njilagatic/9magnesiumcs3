class Animal: # Super Class Animal
    def __init__(self, name):
        self.name = name

    def make_sound(self): # returns sound made by the animal
        pass

    def eat(self): # returns what the animal eats
        pass   

class Lion(Animal): # Subclass Lion that inherits from Animal
    def make_sound(self):
        return f"{self.name} roars loaudly!"

    def feed(self):
        return f"{self.name} eats fresh meat."

class Elephant(Animal): # Subclass Elephant that inherits from Animal
    def make_sound(self):
        return f"{self.name} trumpets!"

    def feed(self):
        return f"{self.name} eats grass and fruits."

class Monkey(Animal): # Subclass Monkey that inherits from Animal
    def make_sound(self):
        return f"{self.name} chatters!"

    def feed(self):
        return f"{self.name} eats bananas."

if __name__ == "__main__":  # main execution
    lion = Lion("Simba")
    elephant = Elephant("Dumbo")
    monkey = Monkey("George")

    # calling methods for each animal 
    print(lion.make_sound())
    print(lion.feed())
    print("-----")

    print(elephant.make_sound())
    print(elephant.feed())
    print("-----")

    print(monkey.make_sound())
    print(monkey.feed())
    print("-----")