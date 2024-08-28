def employee(name, salary=10000):
    tax_multiplier = 0.98
    salary_after_tax = salary * tax_multiplier
    print(f"Employee Name: {name}")
    print(f"Salary After Tax: {salary_after_tax:.2f}")

# Example usage
employee("Lionel Messi")  # Uses default salary
employee("Haris Ahmed", 15000)  # Uses provided salary
