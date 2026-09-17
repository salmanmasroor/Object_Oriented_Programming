"""
Abstraction is the OOP concept of hiding internal implementation details and exposing only the 
essential functionality to the user.

Real-life example

When you use an ATM:

You enter PIN
Select withdrawal
Receive money

You don't need to know the internal banking process.

That is abstraction.
"""
from abc import ABC, abstractmethod

class BankApp(ABC):

    def database(self):
        print("database connected")

    @abstractmethod
    def security(self):
        pass

class MobileApp(BankApp):

    def databse(self): # even if i not defined databse method still obj work beacuse abtractmethod defined. 
        print("database connect")

    def security(self): # i can not create obj of Mobileapp until i define abstractmethod
        print("security set up")

if __name__ == "__main__":
    m = MobileApp()  
    m.database()
    m.security()

    # bank = BankApp() we can not create obj of abstract class