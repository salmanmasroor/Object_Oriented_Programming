"""
Constructor : runs automatically when an object is created.

Attribute: an attribute is a value or property associated with an object.
name and age are attribute of s1 and s2
"""
class Student:
    def __init__(self,name,age): #constructor
        self.name = name #instance variable / attribute
        self.age = age #instance variable / attribute

s1 = Student("Hamza",20)
print(s1.name,s1.age)

s2 = Student("Ali",22)
print(s2.name,s2.age)

