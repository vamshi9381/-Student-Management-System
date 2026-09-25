class Student:

    def __init__(self, student_id, name, age, course, marks):

        self.student_id = str(student_id).strip()
        self.name = str(name).strip()
        self.age = int(age)
        self.course = str(course).strip()
        self.marks = float(marks)

    def __str__(self):
        return (
            f"Student ID: {self.student_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Course: {self.course}, "
            f"Marks: {self.marks}"
        )

    def display(self):

        print(f"ID     : {self.student_id}")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")
        print(f"Marks  : {self.marks}")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["course"],
            data["marks"],
        )