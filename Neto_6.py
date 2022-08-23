class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.ave_grade = 0

    def rate_for_lecturer(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            print("Лектор не найден")
            return
        if course not in self.courses_in_progress:
            print("Вы не являетесь участником данного курса")
            return
        if course not in lecturer.courses_attached:
            print("Лектор не закреплен за данным курсом")
            return
        if grade not in range(1, 11):
            print("Введите оценку по 10-бальной шкале")
            return
        else:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def __str__(self):
        ave_grades(self)
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за домашние задания: {self.ave_grade} \n" \
               f"Курсы в процессе изучения: {self.courses_in_progress} \n" \
               f"Завершенные курсы: {self.finished_courses}"

    def __lt__(person_1, person_2):
        ave_grades(person_1)
        ave_grades(person_2)
        person_1_grade = person_1.ave_grade
        person_2_grade = person_2.ave_grade
        return person_1_grade < person_2_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.ave_grade = 0

    def __str__(self):
        ave_grades(self)
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: {self.ave_grade}"

    def __lt__(person_1, person_2):
        ave_grades(person_1)
        ave_grades(person_2)
        person_1_grade = person_1.ave_grade
        person_2_grade = person_2.ave_grade
        return person_1_grade < person_2_grade


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname}"


def grade_student_comprasion(course, *students):
    student_comprasion = {}
    for student in students:
        ave_grades(student, course=course)
        student_comprasion[student.name, student.surname] = student.ave_grade
    max_grade = 0
    best_student = []
    for student, grade in student_comprasion.items():
        if float(grade) >= max_grade:
            max_grade = grade
    for student, grade in student_comprasion.items():
        if grade == max_grade:
            best_student += student
    if course == "All":
        print(f" Best student on all courses is {best_student} with grade: {max_grade}")
    else:
        print(f" Best student on {course} course is {best_student} with grade: {max_grade}")


def grade_lecturer_comprasion(course, *lecturers):
    lecturer_comprasion = {}
    for lecturer in lecturers:
        ave_grades(lecturer, course)
        lecturer_comprasion[lecturer.name, lecturer.surname] = lecturer.ave_grade
    max_grade = 0
    best_lecturer = []
    for lecturer, grade in lecturer_comprasion.items():
        if float(grade) >= max_grade:
            max_grade = grade
    for lecturer, grade in lecturer_comprasion.items():
        if grade == max_grade:
            best_lecturer += lecturer
    if course == "All":
        print(f" Best lecturer on all courses is {best_lecturer} with grade: {max_grade}")
    else:
        print(f" Best lecturer on {course} course is {best_lecturer} with grade: {max_grade}")


def ave_grades(self, course="All"):
    summ_grade = 0
    grades_amount = 0
    if course != "All":
        for key, value in self.grades.items():
            if course == key:
                for grade in value:
                    summ_grade += int(grade)
                    grades_amount += 1
    else:
        for value in self.grades.values():
            for grade in value:
                summ_grade += int(grade)
                grades_amount += 1
    if grades_amount == 0:
        self.ave_grade = 0
    else:
        ave_grade = round(summ_grade / grades_amount, 2)
        self.ave_grade = ave_grade


# Назначение студентов и менторов
student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']

student_2 = Student('Lev', 'Tolstoy', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Alexander', 'Pushkin')
reviewer_2.courses_attached += ['Git']

lecturer_1 = Lecturer("Vasya", "Pupkin")
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer("Ivan", "The Terrible")
lecturer_2.courses_attached += ['Git']
lecturer_3 = Lecturer("Peter", "The Great")
lecturer_3.courses_attached += ['Git']

# Назначение оценок за занятия
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Git', 7)

student_1.rate_for_lecturer(lecturer_1, "Python", 9)
student_2.rate_for_lecturer(lecturer_1, "Python", 8)
student_2.rate_for_lecturer(lecturer_2, "Git", 6)
student_2.rate_for_lecturer(lecturer_3, "Git", 7)

# Тестирование функций

# grade_student_comprasion("All", student_1, student_2) # передать название курса (либо "All"
# для сравнения по общим оценкам) и студентов через запятую

# grade_lecturer_comprasion("Git", lecturer_1, lecturer_2, lecturer_3)  # передать название курса (либо "All"
# для сравнения по общим оценкам) и лекторов через запятую

# print(lecturer_1)
# print(reviewer_1)
# print(lecturer_1 > lecturer_3)
# print(student_2 > student_1)
