class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Print_biodata(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

student1 = Student("Haris", 20)
student1.Print_biodata()
