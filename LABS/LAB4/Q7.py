class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def calculate_fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def calculate_fare(self):
        base_fare = super().calculate_fare()
        maintenance_fee = base_fare * 0.10
        return base_fare + maintenance_fee

bus = Bus(60)
print(f"Bus Fare: {bus.calculate_fare()}")
