# naomimusalabamisheck
  
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"


class StudentDatabase:
  
    Class representing a database of students.
    Manages adding, removing, and retrieving students.
    """
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]

    def get_student(self, student_id):
        return self.students.get(student_id)

    def get_all_students(self):
        return list(self.students.values())


class StudentService:
    
    Service class that interacts with the StudentDatabase.
    Provides business logic for adding, updating, and deleting students.
    
    def __init__(self, database):
        self.database = database

    def add_new_student(self, student_id, name, age, major):
        student = Student(student_id, name, age, major)
        self.database.add_student(student)

    def delete_student(self, student_id):
        self.database.remove_student(student_id)

    def update_student_info(self, student_id, name=None, age=None, major=None):
        student = self.database.get_student(student_id)
        if student:
            if name:
                student.name = name
            if age:
                student.age = age
            if major:
                student.major = major

    def get_all_students(self):
        return self.database.get_all_students()


class Menu:
    
    Class that provides a simple text-based menu for interacting with the Student Management System.
  
    def __init__(self):
        self.system = StudentService(StudentDatabase())

    def display_menu(self):
        while True:
            print("\nStudent Management System Menu:")
            print("1. Add a new student")
            print("2. Delete a student")
            print("3. Update student information
