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