class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        pass

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20

    def hire(self):
        print(f"{self.name} is hiring someone.")

class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10

    def write_code(self):
        print(f"{self.name} is writing code.")

class SeniorManager(Manager):
    def calculate_bonus(self):
        return self.salary * 0.30

manager = Manager("Haris", 5000)
developer = Developer("Ali", 4000)
senior_manager = SeniorManager("Sabeeh", 7000)

print(f"Manager Bonus: {manager.calculate_bonus()}")
print(f"Developer Bonus: {developer.calculate_bonus()}")
print(f"Senior Manager Bonus: {senior_manager.calculate_bonus()}")
