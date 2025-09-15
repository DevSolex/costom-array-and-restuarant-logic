'''E-Learning System

The e-learning system is a digital platform designed to facilitate online education, 
providing a flexible and accessible learning environment for students and instructors. 
It leverages technology to deliver educational content, interactive learning experiences, 
and collaborative tools through the internet. The system encompasses various features and 
functionalities, including course management, student enrollment, instructor support, 
resource sharing, assessments, and communication tools. In the e-learning system, students 
can access a wide range of courses and educational materials from anywhere, at any time, 
using their personal computers or mobile devices. They can engage in self-paced learning, 
participate in interactive multimedia lessons, and collaborate with peers through discussion 
forums and virtual classrooms. The system provides a student-centered approach, allowing 
learners to progress at their own pace and tailor their learning experience to their individual 
needs. The e-learning system provides numerous benefits, including flexibility in terms of time 
and location, personalized learning experiences, access to a wide range of courses and resources, 
and the ability to accommodate a large number of learners simultaneously. It serves as an 
alternative or complement to traditional classroom-based education, offering convenience, 
scalability, and cost-effectiveness. As technology continues to advance, the e-learning system 
evolves to incorporate new features such as artificial intelligence, virtual reality, and 
adaptive learning algorithms. These advancements enhance the interactivity, personalization, 
and effectiveness of the e-learning experience, further revolutionizing the way education is 
delivered and consumed.
'''


class Management:
    def __init__(self):
        self.courses = []
        self.students = []
        self.instructors = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f'Course {course} already exists.')

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f'Course {course} does not exist.')

    def get_courses(self):
        return self.courses
    
    def add_student(self, student_name):
        if student_name not in self.students:
            self.students.append(student_name)
    
    def remove_student(self, student_name):
        for student in self.students:
            if student_name == student:
                del student
                return '{student_name} remove successful'
            else:
                return '{student_name} is not in students list'
    
    def get_students(self):
        return self.students
    
    def add_instructor(self, instructor_name):
        if instructor_name not in self.instructors:
            self.instructors.append(instructor_name)
        else:
            return f'instructor {instructor_name} already exist'
        
    def remove_instructor(self, instructor_name):
        for instructor in self.instructors:
            if instructor == instructor_name:
                del instructor
                return f'instructor {instructor_name} remove successful'
            else:
                return f"instructor {instructor_name} don'st exist"
            
    def get_instructors(self):
        return self.instructors

mang = Management
mang.add_course('math')

class Student():
    pass
    
class Instructor():
    pass




