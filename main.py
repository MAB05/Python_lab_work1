import math

# task 1
# a = int(input(print("Enter a")))
# for i in range(1, a + 1):
#     print("Number is :", i, "and cube of the", i, "is", i**3)

# task 4
# a = int(input(print("Enter a")))
# j = 0
# for i in range(1, a + 1):
#     j = j + i
# print(j)

# task 3
# a = int(input(print("Enter a")))
# j = 1
# for i in range(1, a + 1):
#     j = j * i
# print(j)

#task2
# list = [10, 20, 30, 40, 50]
# for i in reversed(list):
#     print(i)

#2) Write a function sum_numbers that finds the sum of the first n natural numbers. Make your function recursive
# def sum_numbers(j):
#     if a <= 0:
#         return print("error")
#     else:
#         j = 0
#         for i in range(1, a + 1):
#             j = j + i
#         return
# a = int(input(print("Enter number")))
# if a < 0:
#     print("Enter positive")
# else:
#      print(sum_numbers(j))

# 2) Write a program to use for loop to print the following number pattern
# a = int(input(print("Enter a")))
# for i in range(1, a + 1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# 1) Write a program to use for loop to print the following reverse number pattern
# a = int(input(print("Enter a")))
# for i in range(0, a + 1):
#     for j in range(a - i, 0, -1):
#         print(j, end=" ")
#     print()

# 3) Create a function is_triplet that validates whether
# three given integers form a Pythagorean triplet.
# The sum of the squares of the two smallest integers
# must equal the square of the largest number to be validated.
# def is_triplet(x, y, z):
#     if (x^2) + (y^2) == (z^2):
#         print("Сумма квадратов x и y равна квадрату z")
#     elif (x^2) + (z^2) == (y^2):
#         print("Сумма квадратов x и z равна квадрату y")
#     elif (y^2) + (z^2) == (x^2):
#         print("Сумма квадратов y и z равна квадрату x")
#     else:
#         print("Ошибка")
# is_triplet(x=int(input(print("Enter x"))), y=int(input(print("Enter y"))), z=int(input(print("Enter z"))))