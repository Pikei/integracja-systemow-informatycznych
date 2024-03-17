from Lab2.Animal import Animal


class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        print(f"{self.name} is barking")
