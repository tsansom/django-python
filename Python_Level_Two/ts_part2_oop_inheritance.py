# inheritance

class Animal():

    def __init__(self):
        print('Animal Created')

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')

class Dog(Animal):

    def __init__(self):
        #Animal.__init__(self)
        print('Dog Created')

    def bark(self):
        print('Woof!')

    # This overwrites the previous method
    def eat(self):
        print('Dog Eating')

mydog = Dog()
#these are the inherited methods
#didn't have to define them inside Dog class
mydog.whoAmI()
mydog.eat()
mydog.bark()
