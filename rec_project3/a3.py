class UniversityPerson(object):
    def __init__(self):
        assert type(self) != UniversityPerson, \
                "UniversityPerson class should not be instantiated"

class Student(UniversityPerson):
    def __init__(self, schedule):
        super().__init__()
        self._schedule = schedule

    def add_course(self, course):
        self._schedule.add_course(course)

    def print_schedule(self):
        print(self._schedule)

class Professor(UniversityPerson):
    def __init__(self, schedule):
        super().__init__()
        self._schedule = schedule

    def print_schedule(self):
        print(self._schedule)

class StaffPerson(UniversityPerson):
    def __init__(self, salary):
        super().__init__()
        self._salary = salary

    def get_salary(self):
        return self._salary

class Registrar(StaffPerson):
    def __init__(self, salary, schedule):
        super().__init__(salary)
        self._schedule = schedule

    def print_schedule(self):
        print(self._schedule)

    def add_course(self, course):
        self._schedule.add_course(course)

    def remove_course(self, course):
        self._schedule.remove_course(course)

class Schedule(object):
    def __init__(self, courses):
        self._courses = courses

    def add_course(self, course):
        self._courses.append(course)

    def remove_course(self, name):
        for c in self._courses:
            if c.get_name() == name:
                self._courses.remove(c)

    def __str__(self):
        for c in self._courses:
            print("name:", c.get_name())
            print("hour:", c.get_hour())
            print("--------------------")
        return ""

class Course(object):
    def __init__(self, name, hour):
        self._name = name
        self._hour = hour

    def get_hour(self):
        return self._hour

    def get_name(self):
        return self._name

def main():
    schedule = Schedule([Course("economics", 8), Course("physics", 9), 
        Course("math", 10)])
    student = Student(schedule)
    professor = Professor(schedule)
    staff_person = StaffPerson(50000)
    registrar = Registrar(100000, schedule)

    student.add_course(Course("biology", 11))
    registrar.add_course(Course("english", 12))
    registrar.remove_course("physics")
    
    print("student courses:")
    student.print_schedule()
    print("professor courses:")
    professor.print_schedule()
    print("registrar courses:")
    registrar.print_schedule()
    print("staff_person salary:")
    print(staff_person.get_salary())
    print()
    print("registrar salary:")
    print(registrar.get_salary())
    
main()
