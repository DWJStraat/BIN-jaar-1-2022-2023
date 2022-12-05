class student():

    def __init__(self):
        self.name = None

    def setName(self, name):
        if name.isalpha():
            self.name = name
        else:
            print('Not a name')

    def getname(self):
        return self.name