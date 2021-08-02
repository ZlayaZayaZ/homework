class Student:
    group = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.group.append(self)

    def average_grades(self):
        grades_val = list(self.grades.values())
        _sum = 0
        count = 0
        res = 0
        for grade in grades_val:
            for gr in grade:
                _sum += gr
                count += 1
        if count > 0:
            res = _sum / count
            return round(res, 1)
        return res

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                # lecturer.grades[course] += [grade]
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Not a Student'
        return self.average_grades() >= other.average_grades()

    def __str__(self):
        res = f''' 
    Имя: {self.name}
    Фамилия: {self.surname}
    Средняя оценка за домашние задания: {self.average_grades()}
    Курсы в процессе изучения: {self.courses_in_progress}
    Завершенные курсы: {self.finished_courses}
    '''
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    group = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        Lecturer.group.append(self)

    def average_grades(self):
        grades_val = list(self.grades.values())
        _sum = 0
        count = 0
        res = 0
        for grade in grades_val:
            for gr in grade:
                _sum += gr
                count += 1
        if count > 0:
            res = _sum / count
            return round(res, 1)
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return print('Not a Lecturer')
        return self.average_grades() >= other.average_grades()

    def __str__(self):
        res = f''' 
    Имя: {self.name}
    Фамилия: {self.surname}
    Средняя оценка за лекции: {self.average_grades()}
    '''
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f''' 
    Имя: {self.name}
    Фамилия: {self.surname}
    '''
        return res


def average_grades_group(group, name_courses):
    _sum_ = 0
    count = 0
    result = 0
    for el in group:
        if name_courses in el.grades:
            for grade in el.grades[name_courses]:
                _sum_ += grade
                count += 1
    if count > 0:
        result = _sum_ / count
        return round(result, 1)
    return result


student_sam = Student('Sam', 'Eman', 'man')
student_sam.courses_in_progress += ['Python']

student_lisa = Student('Lisa', 'Edelstein', 'woman')
student_lisa.courses_in_progress += ['Git']
student_lisa.courses_in_progress += ['Python']
student_lisa.add_courses('Введение в программирование')

reviewer_some = Reviewer('Some', 'Buddy')
reviewer_some.courses_attached += ['Python']
reviewer_some.rate_hw(student_sam, 'Python', 8)
reviewer_some.rate_hw(student_sam, 'Python', 10)
reviewer_some.rate_hw(student_sam, 'Python', 5)
reviewer_some.rate_hw(student_lisa, 'Python', 7)
reviewer_some.rate_hw(student_lisa, 'Python', 9)
reviewer_some.rate_hw(student_lisa, 'Python', 6)

reviewer_jesse = Reviewer('Jesse', 'Spencer')
reviewer_jesse.courses_attached += ['Git']
reviewer_jesse.rate_hw(student_lisa, 'Git', 9)
reviewer_jesse.rate_hw(student_lisa, 'Git', 10)
reviewer_jesse.rate_hw(student_lisa, 'Git', 8)

lecturer_omar = Lecturer('Omar', 'Epps')
lecturer_omar.courses_attached += ['Python']
lecturer_omar.courses_attached += ['Git']
student_lisa.rate_hw(lecturer_omar, 'Git', 10)

lecturer_mark = Lecturer('Mark', 'Laurie')
lecturer_mark.courses_attached += ['Git']
student_lisa.rate_hw(lecturer_mark, 'Git', 7)
student_lisa.rate_hw(lecturer_mark, 'Git', 10)

student_sam.rate_hw(lecturer_omar, 'Python', 9)
student_sam.rate_hw(lecturer_omar, 'Python', 4)
student_sam.rate_hw(lecturer_omar, 'Python', 7)

print(student_sam)
print(student_lisa)
print(student_sam < student_lisa)
print(reviewer_some)
print(reviewer_jesse)
print(lecturer_omar)
print(lecturer_mark)
print(lecturer_mark > lecturer_omar)
print('Средняя оценка за домашние задания по курсу Git:', average_grades_group(Student.group, 'Git'))
print('Средняя оценка за домашние задания по курсу Python:', average_grades_group(Student.group, 'Python'))
print('Средняя оценка за лекции по курсу Python:', average_grades_group(Lecturer.group, 'Python'))
print('Средняя оценка за лекции по курсу Git:', average_grades_group(Lecturer.group, 'Git'))
