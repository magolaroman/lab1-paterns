from datetime import datetime
from typing import List, Any


class Course:# про курс

  def __init__(self,title:str,start_date:datetime,end_date:datetime,description:str,lectures:list[str],assignments:list[str],limit:int,students_num:int):
    self.title=title
    self.start_date=start_date
    self.limit = limit
    self.end_date=end_date
    self.description=description
    self.lectures=lectures
    self.assignments=assignments
    self.students:Student = []

    
  #функція видалення студентів із списку
  def delete_student(self, student):
    student.unenroll(self.title)
    self.students.remove(student)
    
  #функція для додавання студентів до списку
  def add_student(self, student: Any):
    if self.limit > len(self.students):
      student.enroll(self)
      self.students.append(student)
      print(f'Student {student.name} as been added to the course {self.title}')
    else:
      print('Too many students')

    
   

class Student:
  """student can enroll any course and can has a lot of progresses """
  def __init__(self, name:str,
               address:str,
               phone_number:str,
               email:str,
               student_number:int) -> None:
    self.name = name
    self.address = address
    self.phone_number = phone_number
    self.email = email
    self.student_number = student_number
    self.average_mark = 0.0
    self.courses: List[Course] = []
    self.course_progress = []
    
    #список курсів,які відвідав студент
  def taken_courses(self):
    return print(f'{self.courses}')

  #функція, за допомогою якої студент може самостійно записатися на будь-який курс
  def enroll(self, course: Course) :
    self.courses.append(course.title)



  #видалення з курсу
  def unenroll(self, course:Course):
    """"""
    self.courses.remove(course)
    print(f'Student {self.name} unenrolled from {course}')

  

class CourseProgres:
  """ course progres of chosen student """
  def __init__(self, received_marks: dict,
               visited_lectures: int,
               assignment:dict):
    self.received_marks = received_marks
    self.visited_lectures = visited_lectures
    self.assignments = {}
    self.assignment = assignment

  #оцінки беруться з отриманих оцінок 
  def get_final_mark(self)->float:
    
    final_mark=sum(self.received_marks.values())/len(self.received_marks)
    return final_mark

  def get_progress_to_date(self, date: datetime):
    marks = [value["mark"] for key, value in self.assignments if date >= key]
    return sum(marks) / len(marks)
 
class Lector:
  def __init__(self,name:str,address:str,phone_number:str,email:str, salary: float, course: Course):
    self.name=name
    self.address=address
    self.phone_number=phone_number
    self.email=email
    self.salary=salary
    self.course = course

  def check_assignment(assignment: dict) -> None:
    if assignment["is_done"]:
      assignment["mark"] = 4.0
      


assignment_1 = {"title": "testing", "description" : "testing", "is_done": False, "mark": 0.0}
assignment_2 = {"title": "testing", "description" : "testing", "is_done": True, "mark": 0.0}


student_1 = Student('Roman','lviv','+380674286233','navi_ma@ukr.net',1000)
course_2 = Course('course_fep',(8,7,2022),(1,12,2022),'nothing',['math','english','programming'],['create proffesionals','develop games','play football'],11,10)
course_1 = Course('course_fei',(8,7,2022),(1,12,2022),'nothing',['math','english','programming'],['create proffesionals','develop games','play football'],11,10)
student_progress_1 = CourseProgres({"english":75,"math":79,"programming":83},3,assignment_1)
lector_1=Lector('Kaskun Oleg','lviv','032265','@dfdf',47.000,course_1)

Lector.check_assignment(assignment_2)
print(assignment_2["mark"])
student_1.enroll(course_1)
course_2.add_student(student_1)
print(student_1.taken_courses())
course_2.delete_student(student_1)
print(student_1.taken_courses())
