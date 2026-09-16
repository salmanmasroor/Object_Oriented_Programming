"""
Encapsulation is the process of wrapping data and methods together inside a class and 
restricting direct access to some data.

You can simply achieve encapsulation in Python by:

Put data inside a class.
Make important data private using __.
Use methods to access or modify that data.

=> private attribute + public method
"""
class Student:
    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def update_name(self,name):
        self.__name = name

if __name__=="__main__":
    s1 = Student("Ali")
    print(s1.__name) # not work beacuse its private attribute 
    print(s1.get_name())
    s1.update_name("hamid")
    print(s1.get_name())