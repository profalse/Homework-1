# number 1 (+)

# print('Как Вас зовут?')
# name = input()
# print('Привет,', name, '!')

# number 2 (+)

# weight = 1.5
# cost_kilo = 41
# money = int(input())
# print('Сдача:', money - cost_kilo * weight)

# number 3 (+)

# weight = float(input())
# cost_kilo = float(input())
# money = float(input())
# print('Сдача:', money - cost_kilo * weight)

# number 4 (?)

# s = 'abcd'
# badc = s[1] + s[0] + s[3] + s[2]
# print(badc)
# print(s.replace('b', 'a', 1).replace('a', 'b', 1).replace('d', 'c', 1).replace('c', 'd', 1))

# number 5 (+)

# f = open('C:/Users/User/МФТИ/Информатика/lesson_1/file.txt', 'w')
# name = 'Сидоров Илья Романович'
# date = '20.01.2006========='
# f.write(name + '\n')
# f.write(date)
# f.close()

# number 6 (В файле input.txt на первой строке перечислены числа (через пробел), на второй строке написан символ арифметической операции (+, -, *), которую необходимо выполнить с ними. Необходимо вывести в файл output.txt результат выполнения арифметической операции.)

# with open('C:/Users/User/МФТИ/Информатика/lesson_1/file_2.txt') as f:
#     numbers = list(map(int, f.readline().split()))
#     operation = f.readline()

# with open('C:/Users/User/МФТИ/Информатика/lesson_1/file_2.txt') as f:
#     if operation == '+':
#         result = sum(numbers)
#     elif operation == '-':
#         result = numbers[0]
#         for num in numbers[1:]:
#             result -= num
#     elif operation == '*':
#         result = 1
#         for num in numbers:
#             result *= num
#     f.write(str(result))