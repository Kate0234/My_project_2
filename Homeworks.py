# Lesson 7.
import re

# Task 1.

# Написати рекурсивну функцію знаходження ступеня числа.

# def power(number, degree):
#     if (degree == 1):
#         return (number)
#     if (degree != 1):
#         return (number * power(number, degree - 1))
# number = int(input("Enter number: "))
# degree = int(input("Enter degree: "))
# print("Result:", power(number, degree))

# Task 2.

# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)


# def stars(n):
#
#    return '' if n<=0 else '*'+stars(n-1)
#
# print(stars(int(input('Enter the number of stars you want to display: '))))

# Task 3.

#Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
#Користувач вводить a та b. Проілюструйте роботу функції прикладом.

# def sum_range(a, b):
#
#     if a > b:
#         return b + sum_range(b+1, a)
#     elif a == b:
#         return a
#     else:
#         return a + sum_range(a+1, b)
#
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
#
# result_of_calculation = sum_range(a,b)
#
# print(result_of_calculation)


#Homework 6. Функції

# Task 1.
# Напишіть функцію, яка обчислює добуток елементів списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

# def mult(n1, n2, n3, n4, n5):
#     mult = n1 * n2 * n3 * n4 * n5
#     print(f"Result of multiplication: {mult}")
# mult(3, 5, 1,7, 8)


# Task 2.
# Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

# def find_minimum(numbers):
#     min_value = numbers[0]
#     for num in numbers:
#         if num < min_value:
#             min_value = num
#     return min_value
#
# numbers_list = [5, 2, 8, 1, 9, 3]
# minimum_value = find_minimum(numbers_list)
# print(f"The minimum value is: {minimum_value}")

# Task 3.
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

# def count_numbers(numbers):
#     return len(numbers)
#
# numbers_list = [5, 2, 8, 1, 9, 3]
# count = count_numbers(numbers_list)
# print(f"The number of elements in the list is: {count}")


# Task 4
# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.

# def remove_number(numbers, target):
#     initial_length = len(numbers)
#     numbers = [num for num in numbers if num != target]
#     deleted_count = initial_length - len(numbers)
#     return numbers, deleted_count

# numbers_list = [5, 2, 8, 1, 9, 3]
# target_number = 8
# updated_list, deleted_count = remove_number(numbers_list, target_number)
# print(f"The updated list is: {updated_list}")
# print(f"Number of elements deleted: {deleted_count}")
#
# # Task 5.
# # Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.
#
# def combine_lists(list1, list2):
#     combined_set = set(list1 + list2)
#     combined_list = list(combined_set)
#     return combined_list
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# combined_list = combine_lists(list1, list2)
# print(f"The combined list is: {combined_list}")
#
#
# #Task 6.
# #Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# # Значення для ступеня передається як параметр, список також передається як параметр.
# # Функція повертає новий список, який містить отримані результати.
#
# def calculate_degrees(numbers, degree):
#     result = [num ** degree for num in numbers]
#     return result
# numbers_list = [1, 2, 3, 4, 5]
# degree = 2
# result_list = calculate_degrees(numbers_list, degree)
# print(f"The result list is: {result_list}")

# Homework 8.

# Task 1. Lомашній номер телефону (тільки цифри та довжина номера)

import re

# def validate_home_phone_number(phone_number):
#
#     pattern = r'^\d{8,12}$'
#
#     if re.match(pattern, phone_number):
#         return True
#     else:
#         return False
#
#
# # Task 2. Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
#
# import re

# def validate_mobile_phone_number(phone_number):
#
#     pattern = r'^\+?\d{12,18}$'
#
#     if re.match(pattern, phone_number):
#         return True
#     else:
#         return False
#
#
# # Task 3. email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
#
# import re

# def validate_email(email):
#
#     pattern = r'^[a-zA-Z0-9_.+-]{1,20}@[a-zA-Z0-9-]{2,5}\.[a-zA-Z]{2,5}$'
#
#     if re.match(pattern, email):
#         return True
#     else:
#         return False
#
#
# #Task 4. ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
#
# import re
#
# def validate_name(name):
#
#     pattern = r'^[a-zA-Z]{2,20}$'
#
#     if re.match(pattern, name):
#         return True
#     else:
#         return False

# def validate_surname(surname):
#
#     pattern = r'^[a-zA-Z]{2,20}$'
#
#     if re.match(pattern, surname):
#         return True
#     else:
#         return False
#
#
# def validate_parental_name(parental_name):
#
#     pattern = r'^[a-zA-Z]{2,20}$'
#
#     if re.match(pattern, parental_name):
#         return True
#     else:
#         return False

#Homework 9.

#Task 1.Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова,
# що складаються не менше ніж з семи літер.

# with open('input.txt', 'w') as file:
#     file.write("Today marks World Vegan Day, and as such our two charts today are tackling the topic. "
#                "Up first, we reveal the cities with the most vegan restaurants per 100,000 inhabitants. "
#                "Our second feature reveals Americans' favorite fake meat products.\n")
#
# with open('input.txt', 'r') as file:
#     text = file.read()
#     words = text.split()
#
# long_words = [word for word in words if len(word) >= 7]

# with open('output.txt', 'w') as file:
#     file.write("\n".join(long_words))
#
# # Task 2. Даний текстовий файл. Підрахувати кількість слів у ньому.
#
# with open('user_input.txt', 'w') as file:
#     pass
#
# user_input = input("Please enter some text: ")
#
# with open('user_input.txt', 'w') as file:
#     file.write(user_input)

# word_count = len(user_input.split())
#
# print(f"The number of words in the text is: {word_count}")


# Hometask 10

class Academy:
    def __init__(self, name):
        self.name = name
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)


class Building:
    def __init__(self, name):
        self.name = name
        self.classrooms = []

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)


class Classroom:
    def __init__(self, number):
        self.number = number
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)


class Teacher:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name):
        self.name = name


class Curriculum:
    def __init__(self, name):
        self.name = name


class Lesson:
    def __init__(self, subject, teacher):
        self.subject = subject
        self.teacher = teacher


class Subject:
    def __init__(self, name):
        self.name = name


class Mark:
    def __init__(self, value):
        self.value = value

if __name__ == "__main__":
    academy = Academy("My Academy")

    building1 = Building("Main Building")
    building2 = Building("Left Building")

    academy.add_building(building1)
    academy.add_building(building2)

    classroom1 = Classroom("201a")
    classroom2 = Classroom("405c")

    building1.add_classroom(classroom1)
    building2.add_classroom(classroom2)

    student1 = Student("Kristian Meller")
    student2 = Student("Jane Doe")

    classroom1.enroll_student(student1)
    classroom2.enroll_student(student2)

    teacher = Teacher("Mr. Smith")

    curriculum = Curriculum("Mathematics")

    subject = Subject("Algebra")

    lesson = Lesson(subject, teacher)

    mark = Mark(11)

    print(f"Academy: {academy.name}")
    print(f"Buildings: {[building.name for building in academy.buildings]}")
    print(f"Classrooms in {building1.name}: {[classroom.number for classroom in building1.classrooms]}")
    print(f"Classrooms in {building2.name}: {[classroom.number for classroom in building2.classrooms]}")
    print(f"Students in Classroom 101: {[student.name for student in classroom1.students]}")
    print(f"Students in Classroom 102: {[student.name for student in classroom2.students]}")
    print(f"Teacher: {teacher.name}")
    print(f"Curriculum: {curriculum.name}")
    print(f"Subject: {subject.name}")
    print(f"Lesson: {lesson.subject.name} with {lesson.teacher.name}")
    print(f"Mark: {mark.value}")








