from enum import Enum

class Action(Enum):
    ADD_STUDENT = 0
    UPDATE_STUDENT_ACTIVITY = 1
    PRINT_ALL = 2
    PRINT_BEST_STUDENT = 3
    PRINT_BAD_STUDENT = 4


class Human:
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class Student(Human):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.test_list = []

    def add_test(self, type, grade):
        self.test_list.append(Test(type, grade))

    def average(self):
        if not self.test_list:
            return 0  # Return 0 if no tests have been added

        total_grade = sum(test.grade for test in self.test_list)
        num_tests = len(self.test_list)
        average_grade = total_grade / num_tests
        return average_grade
    

class Test:
    def __init__(self, type, grade) -> None:
        self.type = type
        self.grade = grade

students = []  # List to store Student instances

def add_student():
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    age = int(input("Enter student's age: "))
    student = Student(f"{first_name} {last_name}", age)
    students.append(student)  # Add student instance to the list
    print("Student added successfully.")

def update_student_activity():
    student_name = input("Enter student's full name: ")
    found = False
    
    for student in students:
        if student_name == student.first_name + " " + student.last_name:
            found = True
            test_type = input("Enter test type: ")
            test_grade = float(input("Enter test grade: "))
            student.add_test(test_type, test_grade)
            print("Test result added successfully.")
            break
    
    if not found:
        print("Student not found.")

def print_all_students(students_list):
    student_averages = []

    for student in students_list:
        avg = student.average()
        student_averages.append((student, avg))

    sorted_students = sorted(student_averages, key=lambda x: x[1], reverse=True)

    print("Students sorted by average:")
    for student, avg in sorted_students:
        print(f"{student.first_name} {student.last_name}: Average = {avg:.2f}")
            
        
def display_menu():
    while(True):
        for action in Action:
            print(f"{action.value}- {action.name.replace('_', ' ')}")
        user_selection = Action( int( input("what 2 do?")))
        if user_selection == Action.EXIT: return
        if user_selection == Action.ADD_STUDENT: add_student()
        if user_selection == Action.UPDATE_STUDENT_ACTIVITY:update_student_activity()
        if user_selection == Action.PRINT_ALL:print_all_students(students)
        if user_selection == Action.PRINT_BAD_STUDENT:pass
        if user_selection == Action.PRINT_BEST_STUDENT:pass
            
    


if __name__ == "__main__":
    display_menu()
