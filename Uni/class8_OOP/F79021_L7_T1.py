class SchoolMember(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super(Teacher, self).__init__(name, age)
        self.salary = salary
        self.courses = {}

    def getSalary(self):
        return self.salary

    def addCourse(self, signature, courseName):
        self.courses[signature] = courseName

    def getCourses(self):
        for key in self.courses:
            print key, self.courses[key]


class Student(SchoolMember):
    def __init__(self, name, age):
        super(Student, self).__init__(name, age)
        self.attendingCourses = {}

    def attendCourse(self, signature, year):
        self.attendingCourses[signature] = {}
        self.attendingCourses[signature]["grades"] = []
        self.attendingCourses[signature]["year"] = year

    def getCourses(self):
        for key in self.attendingCourses:
            print key, self.attendingCourses[key]

    def addGrade(self, signature, grade):
        if signature in self.attendingCourses:
            self.attendingCourses[signature]["grades"].append(grade)

    def getAvgGrade(self, signature):
        sum = 0.0
        for grade in self.attendingCourses[signature]["grades"]:
            sum += grade
        return sum / len(self.attendingCourses[signature]["grades"])
