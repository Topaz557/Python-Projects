from abc import ABC, abstractmethod # here we are importing the ABC module


#assign classes
class Car(ABC): # Here we are creaing the first abstract class that ||| will work as a parent class||??
    def mileage(self):
        pass # this allows us to make classes that inherit the method, however it redines what the method does.

class Tesla(Car):
    def mileage(self):
        print("The mileage is 30mph")

class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25mph")

class Duster(Car):
    def mileage(self):
        print("The mileage is 24 mph")

class Renault(Car):
    def mileage(self):
        print("The mileage is 20 mph")
    
#Driver Code, these are needed for us to call the mileage and print it out

t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()

d = Duster()
d.mileage()
