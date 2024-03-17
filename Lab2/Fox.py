from Lab2.Animal import Animal


class Fox(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

    def sound(self):
        print("What does the fox says?")
