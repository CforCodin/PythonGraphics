class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetail(self):
        print("Name", self.name)
        print("Age", self.age)

    def bark(self):
        print("Woof!")

myDog = Dog("Buddy", 3)
myDog.bark()
myDog.printDetail()

