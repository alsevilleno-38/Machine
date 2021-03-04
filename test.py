class Student:
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @name.deleter
    def name(self):        
        del self.name

s1 = Student("Pam", "None")
print(s1.name)
del s1.name
print(s1.name)
