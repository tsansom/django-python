class Dog():

    # class object attribute (same for all dogs) - immutable
    species = 'mammal'

    # special method starts and ends with __, this ones an initialization method
    # this method refers to itself
    # self.* are attributes
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

mydog = Dog('Chihuahua', 'Sparky')
print('{} is a {}'.format(mydog.name, mydog.breed))
print(mydog.species)
