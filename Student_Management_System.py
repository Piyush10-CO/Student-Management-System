class Student_Management_System:
    def __init__(self, roll, name,  marks):
        self.students = []
        self.roll = roll
        self.name = name
        self.marks = marks
    def display(self):
        print("Student Details:")
        for student in self.students:
            print(f"Name: {student['name']}, Age: {student['age']}, Roll No: {student['roll_no']}")
    def add_student(self):
        print("Enter Student Details:")
        name = input("Name: ")  
        age = int(input("Age: "))
        roll_no = input("Roll No: ")
        student = {
            'name': name,
            'age': age,
            'roll_no': roll_no
        }
        self.students.append(student)
        print("Student added successfully.")
        student = Student_Management_System(self.roll, self.name, self.marks)
        self.display()
    def display_all(self):
        if not self.students:
            print("No students found.")
        else:
            print("All Students:")
            for student in self.students:
                print(f"Name: {student['name']}, Age: {student['age']}, Roll No: {student['roll_no']}")
    def remove_student(self):
        if not self.students:
            print("No students found.")
            return
        roll_no = input("Enter Roll No of student to remove: \n")
        for student in self.students:
            if student['roll_no'] == roll_no:
                self.students.remove(student)
                print("Student removed successfully.\n")
                return
        print("Student not found.\n")
    def search_student(self):
        if not self.students:
            print("No students found.\n")
            return
        roll_no = input("Enter Roll No of student to search: ")
        for student in self.students:
            if student['roll_no'] == roll_no:
                print(f"Student found: Name: {student['name']}, Age: {student['age']}, Roll No: {student['roll_no']}")
                return
        print("Student not found.")     
    def run(self):
        while True:
            print("1.Add Student\n2.Display All Students\n3.Remove Student\n4.Search Student\n5.Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.add_student()  
            elif choice == 2:
                self.display_all()          
            elif choice == 3:
                self.remove_student()   
            elif choice == 4:
                self.search_student()
            elif choice == 5:
                exit()
                break
            else:
                print("Invalid choice. Please try again.")

object = Student_Management_System(0, "", 0)
object.run()    