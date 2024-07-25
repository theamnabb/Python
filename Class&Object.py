# _______________Create a class _________________

class Course: 
    def __init__ (self, course_name, instructor, fee):
        self.course_name = course_name
        self.instructor = instructor
        self.fee = fee

# _______________Method_________________

    def display_info(self):
        print(f"Instructor: {self.instructor}, Course Name: {self.course_name}, Fee: {self.fee}")


# _______________Create Object using contructor _________________

course1 = Course('AaMna', 'Python for beginners','100 Free')
course2 = Course('Fatima', 'Web & Mobile Application for beginners','100 Free')




print(course1.instructor)
(course1.display_info())
(course2.display_info())