#2019112148 김준호

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student1 = Student(2023111111, "Olivia")
student2 = Student(2024111111, "Audrey")

print(student1.student_id, student1.student_name)
print(student2.student_id, student2.student_name)