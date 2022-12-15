class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def main():
    name = input('What is the name of your pet? ')
    animal_type = input('What animal is your pet? ')
    age = int(input('How old is your pet? '))
    pet = Pet(name, animal_type, age)
    print('Here is the data that you entered:')
    print('Name:', pet.get_name())
    print('Animal type:', pet.get_animal_type())
    print('Age:', pet.get_age())