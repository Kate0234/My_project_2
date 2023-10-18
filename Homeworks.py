# Lesson 7.

# Task 1.

# Написати рекурсивну функцію знаходження ступеня числа.

def power(number, degree):
    if (degree == 1):
        return (number)
    if (degree != 1):
        return (number * power(number, degree - 1))
number = int(input("Enter number: "))
degree = int(input("Enter degree: "))
print("Result:", power(number, degree))

# Task 2.

# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)


def stars(n):

   return '' if n<=0 else '*'+stars(n-1)

print(stars(int(input('Enter the number of stars you want to display: '))))

# Task 3.

#Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
#Користувач вводить a та b. Проілюструйте роботу функції прикладом.

def sum_range(a, b):

    if a > b:
        return b + sum_range(b+1, a)
    elif a == b:
        return a
    else:
        return a + sum_range(a+1, b)

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

result_of_calculation = sum_range(a,b)

print(result_of_calculation)