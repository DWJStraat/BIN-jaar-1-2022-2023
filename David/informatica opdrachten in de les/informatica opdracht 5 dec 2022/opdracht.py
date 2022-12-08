class student:

    def __init__(self):
        self.__name = None

    def setName(self, name):
        if name.isalpha():
            self.__name = name
        else:
            print('Not a name')

    def getName(self):
        return self.__name


Jalmar = student()
Jalmar.setName(input('Enter your name: '))

David = student()
David.setName('David')

Nils = student()
Nils.setName('Nils')

Douwe = student()
Douwe.setName('Douwe')

students = [Jalmar, David, Nils, Douwe]

for student in students:
    print(student.getName())
