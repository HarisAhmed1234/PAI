class Employee:
    def get_data(self):
        self.name = input("Enter employee name: ")
        self.monthly_salary = float(input("Enter monthly salary: "))
        self.tax_percentage = float(input("Enter percentage of tax: "))

    def Salary_after_tax(self):
        tax_amount = (self.tax_percentage / 100) * self.monthly_salary
        salary_after_tax = self.monthly_salary - tax_amount
        return salary_after_tax

    def update_tax_percentage(self, new_tax_percentage):
        self.tax_percentage = new_tax_percentage

employee1 = Employee()
employee1.get_data()
print(f"Salary after initial tax: ${employee1.Salary_after_tax():.2f}")
new_tax = float(input("Enter new tax percentage: "))
employee1.update_tax_percentage(new_tax)
print(f"Salary after updated tax: ${employee1.Salary_after_tax():.2f}")
