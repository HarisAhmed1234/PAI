from datetime import datetime

class Vehicle:
    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
        self._rental_price = rental_price
        self.available = True

    def check_availability(self):
        return self.available

    def calculate_rental_cost(self, days):
        return self._rental_price * days

    def rent(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_vehicle(self):
        self.available = True

    def display_details(self):
        return (f"{self.__class__.__name__}: {self.make} {self.model}, "
                f"Price: ${self._rental_price}, Available: {self.available}")

class Car(Vehicle):
    pass

class SUV(Vehicle):
    pass

class Truck(Vehicle):
    pass

class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date

    def display_reservation(self):
        return (f"Reservation for {self.customer.name}: {self.vehicle.display_details()}, "
                f"From: {self.start_date.strftime('%Y-%m-%d')} To: {self.end_date.strftime('%Y-%m-%d')}")

class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self._contact_info = contact_info
        self.rental_history = []

    def rent_vehicle(self, vehicle, start_date, end_date):
        if vehicle.rent():
            reservation = RentalReservation(self, vehicle, start_date, end_date)
            self.rental_history.append(reservation)
            return reservation
        return None

    def return_vehicle(self, vehicle):
        vehicle.return_vehicle()

    def display_rental_history(self):
        return [reservation.display_reservation() for reservation in self.rental_history]

def display_vehicle_details(vehicle):
    print(vehicle.display_details())

def display_reservation_details(reservation):
    print(reservation.display_reservation())

if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 30)
    suv = SUV("Honda", "CRV", 50)
    truck = Truck("Ford", "F-150", 70)

    customer = Customer("Haris Ahmed", "harisahmed@gmail.com")

    display_vehicle_details(car)

    start_date = datetime(2024, 9, 1)
    end_date = datetime(2024, 9, 10)
    reservation = customer.rent_vehicle(car, start_date, end_date)

    if reservation:
        display_reservation_details(reservation)

    print(customer.display_rental_history())
