# Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed= max_speed
        self.mileage=mileage
bike=Vehicle("KTM", 200, 30)
print(bike.max_speed, bike.mileage)