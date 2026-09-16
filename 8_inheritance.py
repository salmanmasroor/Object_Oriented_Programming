"""
Inheritance is an OOP concept in which a child class acquires the properties and
methods of a parent class.

Python supports 5 main types of inheritance:

Single: One parent → One child
Multiple: Two or more parents → One child
Multilevel: Grandparent → Parent → Child
Hierarchical: One parent → Multiple children
Hybrid: Combination of inheritance types

"""

# Single
class Animal:
    def eat(self):
        print("eating")

class Dog(Animal):
    def bark(self):
        print("barking")

d = Dog()
d.eat()
d.bark() 

#Multiple Inheritance
class Father:
    def work(self):
        print("Father works")

class Mother:
    def cook(self):
        print("Mother cooking")

class Child(Father,Mother):
    pass

c = Child()
c.work()
c.cook()

#Multilevel Inheritance
class Grandparent:
    def house(self):
        print("Grandparent's House")

class Parent(Grandparent):
    def car(self):
        print("Parent's car")

class Child(Parent):
    def bike(self):
        print("Bike")

c1 = Child()
c1.house()
c1.car()
c1.bike()
p = Parent()
p.car()
p.house()
#p.bike() error becuase it not have that property or not inherit

#Hierarchical Inheritance
class Animal:
    def eat(self):
        print("eating")

class Dog(Animal):
    def bark(self):
        print("barking")

class Cow(Animal):
    def walk(self):
        print("walking")

d = Dog()
d.eat()
d.bark()

cow = Cow()
cow.eat()
cow.walk()


#Hybrid Inheritance

class Animal:
    def eat(self):
        print("eating")

class Dog(Animal):
    def bark(self):
        print("barking")

class Cow(Animal):
    def walk(self):
        print("walking")

class Puppy(Dog,Cow):
    def jump(self):
        print("jumping")

p = Puppy()
p.eat()
p.bark()
p.walk()
p.jump()