"""
Methods: A method is a function defined inside a class.
It describes the behavior of an object or class.

Python OOP mainly has three types of methods:
1. Instance Method
2. Class Method
3. Static Method

"""

#Instance Method: Works with object/instance data. [self → object data]
class Student:
    school = "XYZ"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print(self.school)

s1 = Student("Ashraf",20)
s1.show()

#Class Method: Works with class-level data.  [cls  → class data]
class Student:
    school = "XYZ"

    @classmethod
    def show_school(cls):
        return cls.school

s2 = Student()
print(s2.show_school())

#Static Method: Does not need object or class data. [none → independent utility]
class Math:

    @staticmethod
    def add(num_one, num_two):
        return num_one + num_two

math = Math()
print(math.add(12,20))