class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def show_details(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.student_name}")

class Marks(Student):
    def __init__(self, student_id, student_name, algo, data_science, calculus):
        Student.__init__(self, student_id, student_name)
        self.algo = algo
        self.data_science = data_science
        self.calculus = calculus

    def show_scores(self):
        print(f"Algorithms: {self.algo}")
        print(f"Data Science: {self.data_science}")
        print(f"Calculus: {self.calculus}")

class Result(Marks):
    def __init__(self, student_id, student_name, algo, data_science, calculus):
        Marks.__init__(self, student_id, student_name, algo, data_science, calculus)

    def calculate_total(self):
        return self.algo + self.data_science + self.calculus

    def calculate_average(self):
        return self.calculate_total() / 3

    def show_final_result(self):
        total = self.calculate_total()
        avg = self.calculate_average()
        self.show_details()
        self.show_scores()
        print(f"Total Score: {total}")
        print(f"Average Score: {avg:.1f}")

# Example usage
student = Result(236005, "Haris Ahmed", 88, 99, 77)
student.show_final_result()
