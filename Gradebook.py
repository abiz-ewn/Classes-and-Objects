"""
This program serves as a gradebook for students, in which teachers will find it easy to implement while working on students grades.
By: Abigail Ewnetu
"""
class EmptyRosterError(Exception):
    def __init__(self):
        Exception.__init__(self, "Error: Course Roster is Empty!")
        print("Error: Course Roster is Empty!")

class StudentNotFoundError(Exception):
    def __init__(self, student_id):
        Exception.__init__(self, f"Error: Student ({student_id}) not found")
        print(f"Error: Student ({student_id}) not found")

class GradeItemNotFoundError(Exception):
    def __init__(self, item_name):
        Exception.__init__(self, f"Error: Grade Item ({item_name}) not found")
        print(f"Error: Grade Item ({item_name}) not found")

#Student Class

class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

#GradeItem Class

class GradeItem:
    def __init__(self, name, total_points):
        self.name = name
        self.total_points = total_points
        self.grades = {}

    def add_student_grade(self, student_id, grade):
        self.grades[student_id] = grade

    def get_name(self):
        return self.name

    def get_total_points(self):
        return self.total_points

    def get_student_grade(self, student_id):
        return self.grades.get(student_id, None)

# Course Class 

class Course:
    def __init__(self):
        self.roster = []
        self.grade_items = []

    def add_student(self, student):
        self.roster.append(student)

    def add_grade_item(self, item):
        self.grade_items.append(item)

    def add_student_grade(self, item_name, student_id, grade):
        if self.roster == []:
            raise EmptyRosterError()

        student = None
        for s in self.roster:
            if s.get_student_id() == student_id:
                student = s
                break
        if student is None:
            raise StudentNotFoundError(student_id)

        item = None
        for g in self.grade_items:
            if g.get_name() == item_name:
                item = g
                break
        if item is None:
            raise GradeItemNotFoundError(item_name)

        item.add_student_grade(student_id, grade)

    def print_student_grades(self, student_id):
        if self.roster == []:
            raise EmptyRosterError()

        student = None
        for s in self.roster:
            if s.get_student_id() == student_id:
                student = s
                break
        if student is None:
            raise StudentNotFoundError(student_id)

        print(f"\n{student.get_last_name()}, {student.get_first_name()} ({student_id})", end=" | ")
        for item in self.grade_items:
            grade = item.get_student_grade(student_id)
            grade_display = grade if grade is not None else "N/A"
            print(f"{item.get_name()}: {grade_display} ({item.get_total_points()})", end=" | ")
        print()

    def print_roster(self):
        if self.roster == []:
            raise EmptyRosterError()

        print("\nCourse Roster:")
        for student in self.roster:
            print(f"{student.get_last_name()}, {student.get_first_name()} ({student.get_student_id()})")

    def print_class_grades(self):
        if self.roster == []:
            raise EmptyRosterError()

        print("\nClass Grades:")
        for student in self.roster:
            print(f"{student.get_last_name()}, {student.get_first_name()} ({student.get_student_id()})", end=" | ")
            for item in self.grade_items:
                grade = item.get_student_grade(student.get_student_id())
                grade_display = grade if grade is not None else "N/A"
                print(f"{item.get_name()}: {grade_display} ({item.get_total_points()})", end=" | ")
            print()


def main():
    course = Course()

    # Prints the Menu
    print("Welcome to the Gradebook System!")
    print("Please choose one of the following options:")
    print("1) Add a Student")
    print("2) Add a Grade Item")
    print("3) Add a Student's Grade")
    print("4) Print a Student's Grades")
    print("5) Print Course Roster")
    print("6) Print Class Grades")
    print("Enter 'q' or 'quit' to exit")

    while True:
        print(":> ", end='')
        choice = input().strip().lower()

        if choice in ['q', 'quit']:
            break

        try:
            if choice == '1':
                first = input("Enter First Name: ").strip()
                last = input("Enter Last Name: ").strip()
                try:
                    student_id = int(input("Enter Student ID: ").strip())
                except ValueError:
                    print("Error: Enter an integer Student ID")
                    continue
                course.add_student(Student(first, last, student_id))

            elif choice == '2':
                name = input("Enter grade item name: ").strip()
                try:
                    total = int(input("Enter the total points for the grade item: ").strip())
                except ValueError:
                    print("Error: Enter a numeric value for total points.")
                    continue
                course.add_grade_item(GradeItem(name, total))

            elif choice == '3':
                item_name = input("Enter grade item name: ").strip()
                try:
                    student_id = int(input("Enter Student ID: ").strip())
                except ValueError:
                    print("Error: Enter an integer Student ID")
                    continue
                try:
                    grade = float(input("Enter Student Grade: ").strip())
                except ValueError:
                    print("Error: Enter a numeric grade.")
                    continue
                course.add_student_grade(item_name, student_id, grade)

            elif choice == '4':
                try:
                    student_id = int(input("Enter Student ID: ").strip())
                except ValueError:
                    print("Error: Enter an integer Student ID")
                    continue
                course.print_student_grades(student_id)

            elif choice == '5':
                course.print_roster()

            elif choice == '6':
                course.print_class_grades()

            else:
                print("Invalid option. Please enter 1-6, or 'q' to quit.")

        except (EmptyRosterError, StudentNotFoundError, GradeItemNotFoundError):
            continue

if __name__ == "__main__":
    main()
