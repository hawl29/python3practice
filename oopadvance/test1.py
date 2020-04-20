from types import MethodType

class Student(object):
    __slots__ = ('name','age','score','set_age')


s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self,age):
    self.age = age

s.set_age = MethodType(set_age,s)

s.set_age(25)
print(s.age)

def set_score(self,score):
    self.score = score

Student.set_score = set_score

s.set_score(99)

print(s.score)

class GraduateStudent(Student):
    __slots__ = ('gender')


g = GraduateStudent()
g.gender = 'female'
g.name = 'abc'

print(g.name)
