"""
Constructor : runs automatically when an object is created.

"""
class Student:
    def __init__(self,name,age): #constructor
        self.name = name #instance variable
        self.age = age

s1 = Student("Hamza",20)
print(s1.name,s1.age)

s2 = Student("Ali",22)
print(s2.name,s2.age)

