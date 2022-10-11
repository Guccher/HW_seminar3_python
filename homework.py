#  Task № 1
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# numeric_list = [2, 3, 5, 9, 3]
# amount = 0
# for i in range(len(numeric_list)):
#     if i % 2 !=0:
#      amount = amount + numeric_list[i]
# print(amount)


# Task  № 2
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint

# number = int(input('Enter n: '))
# numeric_list = []
# result_list = []
# temp = 0
# for i in range(number):
#     numeric_list.append(randint(0,5))

# for i in range((len(numeric_list)+1)//2):
#     temp = numeric_list[i]
#     numeric_list[i] = numeric_list[len(numeric_list) - 1 - i]
#     numeric_list[len(numeric_list) - 1 - i] = temp
#     result_list.append(numeric_list[i] * numeric_list[len(numeric_list) - 1 - i] )
# print(numeric_list)
# print(result_list)


# Task № 3
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
#  и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random

# fractional_list = []
# size_list = int(input('Enter size: '))
# fractional_list=[round(random.uniform(0, 30), 2) for i in range(size_list)]
# print(fractional_list)

# maximal_value = fractional_list[0]
# minimal_value = fractional_list[0]
# subtraction = 0
# for i in range(len(fractional_list)):
#     if (minimal_value > fractional_list[i]):
#         minimal_value = fractional_list[i]
#     if (maximal_value < fractional_list[i]):
#         maximal_value = fractional_list[i]
#     subtraction = maximal_value - minimal_value
# print('subtraction between maximum and minimum values =', subtraction)
# print('minimal value in list =', minimal_value)
# print('maximal value in list =', maximal_value)

# Task № 4
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

#  Variant 1
# decimal_number = int(input('Enter number: '))
# remains = ''
# while decimal_number > 0:
#     remains = str(decimal_number % 2) + remains
#     decimal_number = decimal_number // 2
# print(remains)

# Variant 2
# print(str(bin(int(input())))[2:])


# Task № 5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# fibonacci0 = 0
# fibonacci1 = fibonacci2 = 1
# negative_fibonacci_number = int (input('Enter negative number row fibonacci: '))
# positive_fibonacci_number = int  (input('Enter positive number row fibonacci: '))
# fibonacci_list = []
# fibonacci_list1 = []
# while (negative_fibonacci_number <= fibonacci0):
#    fibonacci1, fibonacci2 = fibonacci2, fibonacci1 - fibonacci2
#    negative_fibonacci_number += 1
#    fibonacci_list.append(fibonacci2)
#    string = fibonacci_list[::-1]
# print(string)

# fibonacci1 = fibonacci2 = 1
# positive_fibonacci_number = int(positive_fibonacci_number - 2) 
# fibonacci_list1.append(fibonacci1)
# while (positive_fibonacci_number > fibonacci0):
#    fibonacci1, fibonacci2 = fibonacci2, fibonacci1 + fibonacci2
#    positive_fibonacci_number -= 1
#    fibonacci_list1.append(fibonacci2)
# print(fibonacci_list1)
# print(string + fibonacci_list1)

