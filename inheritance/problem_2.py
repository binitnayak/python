class animal:
    pass
class pets(animal):
    pass
class Dog(pets):
    @staticmethod
    def bark():
        print('Bow bow')

d=Dog()
d.bark()