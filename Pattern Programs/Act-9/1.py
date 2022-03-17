"""Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.
seating_capacity() a default value of 50"""
n=(input())
class Vehicle:
    def seating_capacity(capacity):
        pass
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        d=f"The seating capacity  is {capacity} passengers"
        print(d)
buss = Bus()
if n == "":
    buss.seating_capacity()
else:
    buss.seating_capacity(n)