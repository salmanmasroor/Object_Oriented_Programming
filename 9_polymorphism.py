"""
Polymorphism means “many forms.” In OOP, it allows the same method, function, 
or interface to behave differently depending on the object or data it is working with.

In Python, it is commonly achieved through duck typing, method overriding, and operator 
overloading.

Common types of polymorphism in Python
-Duck typing
-Method overriding
-Operator overloading
-Function polymorphism through built-in functions
"""

#Duck Typing: Python focuses on what an object can do, not its exact type.

class Duck:
    def fly(self):
        print("Duck Flying")

class Bird:
    def fly(self):
        print("Bird Flying")

def make_fly(obj):
    obj.fly()

make_fly(Duck())
make_fly(Bird())

#Method overriding: A child class provides its own implementation of a parent method.

class Animal:
    def speak(self):
        print("Animal speak")

class Dog(Animal):
    def speak(self):
        print("Bark")

dog = Dog()
dog.speak()

animal = Animal()
animal.speak()

#Operator polymorphism: The same operator works differently with different data types:

print(2 + 3)          # 5
print("Hi " + "Ali")  # Hi Ali
print([1] + [2])      # [1, 2]