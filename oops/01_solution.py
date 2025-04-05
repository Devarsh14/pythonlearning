class Person:
    name = "dharmika"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()

# a.name = "Devarsh"
# a.occupation ="Accountant"
a.info()
