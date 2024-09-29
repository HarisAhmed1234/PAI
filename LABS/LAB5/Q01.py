class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        maintenance_charge = 0.1 * total_fare
        return total_fare + maintenance_charge


bus = Bus(seating_capacity=50)
print("Total fare for the bus:", bus.fare())
