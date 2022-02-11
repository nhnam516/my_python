class Vehicle:
    def __init__(self,name,max_speed,mileage,capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self,capacity):
        return f"The capacity of {self.name} is {capacity}people."

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def seating_capacity(self, capacity):
        return super().seating_capacity(capacity=50)

car1 = Vehicle("Yellow car",100,200,4)
bus1 = Bus("Red bus",80,300,48)

print(f"{car1.name} max speed is {car1.max_speed}km/h")
print(f"{bus1.name} mileage is {bus1.mileage} km, it can take "
      f"{bus1.seating_capacity(40)} people")

print("total bus fare is: " + str(bus1.fare()))