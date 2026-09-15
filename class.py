"""
Definition: A class is a blueprint for creating objects. 
It groups data (attributes) and behavior (methods) together.
"""
#Class
class Student:
    def show(self):
        print("I am a student.")

s1 = Student()
s1.show()

#Constructor
class Student:
    def __init__(self,name,age): #constructor: runs automatically when an object is created.
        self.name = name #instance variable
        self.age = age

s2 = Student("Hamza",20)
print(s2.name,s2.age)

#self : refers to the current object.
class Car:
    def start(self):
        print("Car start")

    def stop():
        print("car stop")

    @staticmethod
    def move():
        print("car is moving")

car = Car()
car.start()
# car.stop() it not work because no self
Car.stop() 

Car.move() # it work because staticmethod now using decorator

#instanse method
class Car:
    def start(self):
        print("ccar is start")

c1 = Car()
c1.start()

#instance variable: An instance variable belongs to a specific object.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("shahid",22)
s2 = Student("Hamid",23) #s1 amd s2 have thier own name and age 

print(s1.name,s1.age," ",s2.name,s2.age)

#Class variable: A class variable belongs to the class and is shared by objects.
class Student:
    school = "XYZ"
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("shahid",22)
s2 = Student("Hamid",23) #s1 amd s2 have thier own name and age 
print(s1.school,s2.school) # shared common object

#Class Method: Used when you need to work with class-level data.
class Student:
    student = "XYZ"

    @classmethod
    def call(cls):
        print(cls.student)

s1 = Student()
s1.call()