#!/usr/bin/env python3
"""Base Animal class for this wonderfully simple Animal Kingdom"""

class Animal():
    """Base class for our animal kingdom"""

    alive = True
    nb_animals = 0
    All_the_animals = {}

    def __init__(self, name = None, age = None, blood_temp = None, id = None):
        """ Initializes information for base class
        """
        self.name = name
        self.age = age
        self.blood_temp = blood_temp

        if id is not None:
            self.id = id
        else:
            Animal.nb_animals += 1
            self.id = Animal.nb_animals

    def eat(self):
        """Method for displaying that the animal is eating"""
        print(self.name + " is grubbin' down")
        
    def sleep(self):
        """Method for displaying that the animal is sleeping"""
        print("No rest for the wicked... except for " + self.name + ". Big sleepy.")

    @classmethod
    def log_animal(cls, name):
        """logs animal"""
        Animal.All_the_animals[name] = cls.__name__
        

class Mammal(Animal):
    """Class for Mammals"""

    def __init__(self, name=None, age=None, blood_temp="Warm", weight=None):
        """Sets the attritubes to the mammal class"""
        super().__init__(name, age, blood_temp)
        super().log_animal(name)


class Reptile(Animal):
    """Class for Reptiles"""

    def __init__(self, name=None, age=None, blood_temp="Cold", weight=None):
        """Sets the attritubes to the Reptile class"""
        super().__init__(name, age, blood_temp)
        super().log_animal(name)
    
    def appearance(self):
        """displays the creature"""
        
        print("")


human = Mammal('Aaron', 30, 'Hot', 206)
human2 = Mammal('Ben', 35, 'Cold', 190)
LizardBoy = Reptile('Larry', 1, weight=4)

print(human.alive)
print(human2.alive)
human.eat()
human.sleep()
print(human.nb_animals)
LizardBoy.appearance()
print(Animal.All_the_animals)
print(Animal.nb_animals)

