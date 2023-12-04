class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species

    def speak(self):
        print(f'{self.name} is an {self.species} and makes a sound.')

class Dog(Animal):
    def __init__(self, name, breed) -> None:
        super().__init__(name, species='Dog')
        self.breed = breed

    def speak(self):
        print(f'{self.name} is a {self.breed} dog and barks.')

class Cat(Animal):
    def __init__(self, name, breed) -> None:
        super().__init__(name, species='Cat')
        self.breed = breed

    def speak(self):
        print(f'{self.name} is a {self.breed} cat and meeow.')