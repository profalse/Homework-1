# Number 1 (вывод треугольника)
# С помощью цикла
# my_string = "python"
# x = 0

# for i in my_string:
#     x = x + 1
#     print(my_string[0:x])

# for i in my_string:
#     x = x - 1
#     print(my_string[0:x])

# # С помощью функции
# def print_triangle(size, symb):
#     for i in range(1, size + 1):
#         print(symb * i)
#     for i in range(size - 1, 0, -1):
#         print(symb * i)

# print_triangle(5, '*')


# Number 2 (разложение числа на простые множители)
# через цикл
# number = int(input("Введите целое число: "))
# n = number
# k = 2
# factor = []
# while number/k >= 1:
#     if number == 1: print("1 не простое число")
#     if number % k == 0:
#         number = number/k
#         factor.append(k)
#     else: k += 1
# print(f"Простые множители числа {n}: {factor}")

# через функцию
# number = int(input("Введите целое число: "))
# def prime_number(n):
#     factor = []
#     k = 2
#     while n/k >= 1:
#         if n == 1: print("1 не простое число")
#         if n % k == 0:
#             n = n//k
#             factor.append(k)
#         else: k += 1
#     return factor
# result = prime_number(number)
# print(f"Простые множители числа {number}: {result}")


# Number 3 (Программа, считающая коэффициенты МНК для набора измерений x и y)
# y = a*x + b
# import numpy as np
# x = np.array(list(map(float, input().split())))
# y = np.array(list(map(float, input().split())))
# n = len(x)

# a = (n * sum(x * y) - sum(x) * sum(y))/(n * sum(x**2) - (sum(x))**2)
# b = (sum(y) - a * sum(x))/n

# print(a)
# print(b)