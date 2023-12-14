class student:
    school_name='ABC school'
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("james",26)
print('student:',s1.name,s1.age)
print('school name:',student.school_name)
s1.name='bond'
s1.age=19
print('student name:',s1.name,s1.age)
student.school_name='xyz  school'
print("school name:",student.school_name)
