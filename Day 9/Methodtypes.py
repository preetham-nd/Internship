class Student:
    
    college_name = "ABC College"


    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name


    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"


    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)



student1 = Student("Rahul", 101)
student2 = Student("Anita", 102)


student1.display()
student2.display()

Student.change_college("XYZ College")


student1.display()
student2.display()


print("Rahul Result:", Student.is_pass(78))
print("Anita Result:", Student.is_pass(30))
