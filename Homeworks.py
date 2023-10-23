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

def mult(n1, n2, n3, n4, n5):
    mult = n1 * n2 * n3 * n4 * n5
    print(f"Result of multiplication: {mult}")
mult(3, 5, 1,7, 8)


# Task 2.
# Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

def find_minimum(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

numbers_list = [5, 2, 8, 1, 9, 3]
minimum_value = find_minimum(numbers_list)
print(f"The minimum value is: {minimum_value}")

# Task 3.
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

def count_numbers(numbers):
    return len(numbers)

numbers_list = [5, 2, 8, 1, 9, 3]
count = count_numbers(numbers_list)
print(f"The number of elements in the list is: {count}")


# Task 4
# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.

def remove_number(numbers, target):
    initial_length = len(numbers)
    numbers = [num for num in numbers if num != target]
    deleted_count = initial_length - len(numbers)
    return numbers, deleted_count

numbers_list = [5, 2, 8, 1, 9, 3]
target_number = 8
updated_list, deleted_count = remove_number(numbers_list, target_number)
print(f"The updated list is: {updated_list}")
print(f"Number of elements deleted: {deleted_count}")

# Task 5.
# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.

def combine_lists(list1, list2):
    combined_set = set(list1 + list2)
    combined_list = list(combined_set)
    return combined_list

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
combined_list = combine_lists(list1, list2)
print(f"The combined list is: {combined_list}")


#Task 6.
#Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.

def calculate_degrees(numbers, degree):
    result = [num ** degree for num in numbers]
    return result
numbers_list = [1, 2, 3, 4, 5]
degree = 2
result_list = calculate_degrees(numbers_list, degree)
print(f"The result list is: {result_list}")