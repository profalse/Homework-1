# Работа с файлами

# f = open('C:/Users/Koles/Desktop/text.txt', 'w')
# f.write("Kolesnicova Olga Pavlovna\n")
# f.write("21.08.2001")
# f.close()

# with open('C:/Users/Koles/Desktop/text', 'w') as f:
#     f.write("Kolesnikova Olga Pavlovna")
#     f.write("21.08.2001")

# Цикл for

# my_string = "python"
# x = 0

# for i in my_string:
#     x = x + 1
#     print(my_string[0:x])

# for i in my_string:
#     x = x - 1
#     print(my_string[0:x])


# print(9 << 1)
# print(9 >> 1)
# print(bin(9))

# oct() - функция перевода в восьмизначную систему счисления
# hex() - функция перевода в четырнадцатизначную систему счисления
# xex() - функция перевода в шестнадцатизначную систему счисления
# print(oct(112))

# n = bin(5)
# print(int(n, 2)) # переводит из некоторой системы счисления в десятичную

# ------------------------------------------------------------------------------------

# наполнение списка числами с шагом 5
# a = []
# for i in range(1, 100, 5):
#     a.append(i)
# print(a)

# a = [i for i in range(1, 10)]
# print(a)

# a = [i**2 for i in range(10) if i % 2 == 0]
# print(a)

# a = "lsj94ksd231 9"
# b = [int(i) for i in a if '0' <= i <= '9']
# print(b)

# Таблица основных функций для работы со списками

# x in A        
# x not in A
# min(A)/max(A)
# sum(A)
# A.index(x)
# A.count(x)
# A.append(x)
# A.insert(i, x)
# A.pop(x)
# A.pop()
# A.extend(B)

# Форматирование строк

