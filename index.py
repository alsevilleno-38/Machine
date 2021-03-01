class Student:
    def __init__(self, name):
        self.name = name

class PhD(Student):
    def __init__(self, name, field):
        super().__init__(name)
        self.field = field
    
p1 = PhD("Doe", "Math")
print(p1.name)
print(p1.field)


