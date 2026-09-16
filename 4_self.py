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

car.move() # it work because staticmethod now using decorator
