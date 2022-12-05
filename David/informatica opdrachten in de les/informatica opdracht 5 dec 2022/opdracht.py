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
