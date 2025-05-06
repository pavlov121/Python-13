# print("Задание №1")
# # Задание №1 (Использовал while !)
# num = int(input("Введите пятизначное число: "))
# s = 0
# s1 = 1
# s2 = 0
# if 1000 <= num <= 99999:
#     s = num
#     while s != 0:
#         s1 = s % 10 * s1
#         s2 += s % 10
#         s = s // 10
#     s2 = s2 // 5
#     print("Произведение цифр числа", num, ":", s1, sep=" ")
#     print("Среднее арифметическое цифр числа", num, ":", s2, sep=" ")
# else:
#     print("Ошибка!")
#
# print("\nЗадание №2")
# # Задание №2
# num1 = int(input("Введите число от 1 до 99: "))
# if 1 <= num1 <= 99:
#     if num1 % 10 == 1 and num1 != 11:
#         print(num1, "копейка")
#     if num1 % 10 == 2 and num1 != 12:
#         print(num1, "копейки")
#     if num1 % 10 == 3 and num1 != 13:
#         print(num1, "копейки")
#     if num1 % 10 == 4 and num1 != 14:
#         print(num1, "копейки")
#     else:
#         print(num1, "копеек")
# else:
#     print("Число нецелое или не входит в диапазон!")

# print("\nЗадание №3")
# # Задание №3(Использовал исключение!)
#
# n = input("Количество символов: ")
# m = input("Тип символа: ")
# print("0 - горизонтальная\n1 - вертикальная")
# c = input("ориентация линии: ")
# try:
#     i = 0
#     n = int(n)
#     c = int(c)
#     while i < n:
#         if c == 0:
#             print(m, end="")
#         else:
#             print(m)
#         i += 1
# except ValueError:
#     print("Что-то пошло не так! Введен символ!")
# else:
#     print("\nПрограмма выполнена успешно!")

# print("\nЗадание #4")
# # Задание №4
# s = 0
# n = [int(input("-> ")) for i in range(int(input("n = ")))]
# for i in n:
#     if i == 0:
#         continue
#     else:
#         s += i
# sr_arif = s / (len(n))
# print("Среднее арифметическое:", sr_arif)

# import random
# print("\nЗадание №5")
# # Задание №5
#
# n = int(input("Ввести самому(1) или автоматически(0): "))
# if n == 1:
#     m = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
#     print("Список:", m)
#     z1 = []
#     for i in m:
#         if i > 0:
#             z1.append(i)
#     print("Новый список, состоящий из положительных элементов:", z1)
#     print("Наибольший элемент списка:", max(z1))
# else:
#     c = [random.randint(-10, 10) for j in range(int(input("Введите длину списка: ")))]
#     print("Список:", c)
#     z2 = []
#     for j in c:
#         if j > 0:
#             z2.append(j)
#     print("Новый список, состоящий из положительных элементов:", z2)
#     print("Наибольший элемент списка:", max(z2))


# from math import pi  # Для pi
# print("\nЗадание №6")
# # Задание №6
#
#
# def s_rectangle():  # Прямоугольник
#     x = int(input("Сторона a: "))
#     y = int(input("Сторона b: "))
#     s = x * y
#     print("Площадь прямоугольника: ", s, sep="")
#
#
# def s_triangle():  # Треугольник
#     x1 = int(input("Основание: "))
#     y1 = int(input("Высота: "))
#     s1 = 0.5 * x1 * y1
#     print("Площадь треугольника: ", s1, sep="")
#
#
# def s_circle():
#     x2 = int(input("Радиус: "))
#     s2 = pi * x2 ** 2
#     print("Площадь круга: ", s2, sep="")
#
#
# try:
#     a = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
#     if a == 1:
#         s_rectangle()
#     if a == 2:
#         s_triangle()
#     if a == 3:
#         s_circle()
# except TypeError:
#     print("Ошибка! Был введён символ или введена не та цифра!")
# else:
#     print("\nКонец программы!")

# print("\nЗадание №7")
# # Задание №7
# s1 = input("Введите первую строку: ")
# s2 = input("Введите вторую строку: ")
# s3 = set(s1) - set(s2)  # Элементы входящие в s1, но не входящие в s2
# print("Искомыми буквами являются: ")
# for i in s3:
#     print(i, end=" ")

# print("\nЗадание №8")
# # # Задание №8
# sp = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#       "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#       "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#       "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2694}}
#
# for i, j in sp.items():
#     print(i)
#     for s, d in j.items():
#         print(s, ":", d)
#
# name = input("Имя: ")
# reg = input("Регион: ")
# while True:
#     if sp[name][reg]:
#         print(sp[name][reg])
#     else:
#         print("Нет таких данных!")
#     break
#
# try:
#     new = int(input("Новое значение: "))
#     sp[name][reg] = new
#     print(sp[name])
# except ValueError:
#     print("Введите число!")
# finally:
#     print("\nКонец программы!")


# print("\nЗадание №9")
# # # Задание №9
#
#
# def sr_zn(x, y):  # Функция, вычисляет среднее значение и производит поиск
#     all = dict(zip(x, y))
#     k = dict()  # отборочный список
#     count = 0  # счётчик баллов
#     s = 0  # количество студентов
#     sr = 0  # среднее значение
#     for i in all:  # Вычисление среднего значения
#         count += all[i]
#         s += 1
#     sr = round(count / s)
#     for j in all:  # Произведение поиска
#         if all[j] >= sr:
#             k[j] = all[j]
#     print("\nСредний балл: ", sr, ". Студенты с баллом выше среднего: \n", sep="")
#     for s in k:  # Перебор студентов с баллом > sr
#         print(s)
#
#
# try:  # Основная программа
#     stud = []  # Список студентов
#     ball = []  # Список баллов
#     n = 1  # Счётчик студентов
#     m = int(input("Количество студентов: "))
#     while True:
#         if n <= m:
#             print(n, end="")
#             stud.append(input("-й студент: "))
#             ball.append(int(input("Балл: ")))
#             n += 1
#         else:
#             break
#     sr_zn(stud, ball)
# except TypeError:
#     print("Введён символ!")
# finally:
#     print("\nКонец программы!")

# print("\nЗадание №10")
# # # Задание №10
#
# s_0 = 0  # глобальная переменная
#
#
# def s1():
#     global s_0
#
#     def per1():
#         a = [int(input(" ")) for i in range(0, 3)]
#         n = a[0] * a[1]
#         m = a[1] * a[2]
#         c = a[0] * a[2]
#         return n + m + c
#
#     s_0 = 2 * per1()
#     print("Площадь поверхности (как глобальная переменная):", s_0)
#
#
# def s2():
#     s_1 = 0  # Локальная переменная
#
#     def per2():
#         a2 = [int(input(" ")) for i in range(0, 3)]
#         n2 = a2[0] * a2[1]
#         m2 = a2[1] * a2[2]
#         c2 = a2[0] * a2[2]
#         return n2 + m2 + c2
#
#     s_1 = 2 * per2()
#     print("Площадь поверхности (как локальная переменная):", s_1)
#
#
# def s3():
#     s_3 = 0
#
#     def per3():
#         nonlocal s_3  # Нелокальна переменная
#         a3 = [int(input(" ")) for i in range(0, 3)]
#         n3 = a3[0] * a3[1]
#         m3 = a3[1] * a3[2]
#         c3 = a3[0] * a3[2]
#         s_3 = 2 * (n3 + m3 + c3)
#         print("Площадь поверхности (как локальная переменная):", s_3)
#     per3()
#
#
# s1()  # Глобальная
# s2()  # Локальная
# s3()  # Нелокальная


# print("\nЗадание №11")
# # Задание №11
#
#
# def decor(fn):  # Декоратор, принимающий функцию fn
#     def wrap(arg1):  # Внутренняя функция, принимающая список arg1
#         a = ", ".join(map(str, arg1))  # Цикл перевода каждого элемента в тип str, перечисление через запятую
#         print("Сумма чисел: ", a, "=", fn(arg1), "\nСреднее арифметическое чисел: ", a, "=", (fn(arg1) // len(arg1)))
#         return f"Конец программы!"
#     return wrap
#
#
# @decor
# def su(sp):  # Функция вычисления
#     return sum(sp)
#
#
# try:  # Основная программа
#     n = int(input("Количество чисел: "))
#     chis = [int(input("->")) for i in range(1, n+1)]
#     print(su(chis))
# except TypeError:
#     print("Ошибка!")

# print("\nЗадание №12")
# # Задание №12
#
# try:
#     a = input("Введите строку: ")
#     a = a.replace('о', "О")
#     s1 = a.find("О")  # первое вхождение
#     print("Индекс первого совпадения", s1)
#     s2 = a.rfind("О")  # второе вхождение
#     print("Индекс второго совпадения", s2)
#     print("После замены всех 'о' на 'О': ", a)
#     a1 = ""
#     for i in range(0, len(a)):
#         if i == s1 or i == s2:
#             a1 += a[i].lower()
#         else:
#             a1 += a[i]
#     print("После выполнения: ", str(a1))
# except TypeError:
#     print("Не строка!")

# print("Добрый вечер!)")

# import re
#
# print("\nЗадание №14")
# # Задание №14
#
#
# def validate_login(password):
#     return re.findall(r"^[A-Za-z0-9-@_]{6,18}$", password)
#
#
# text = input("Введите пароль: ")
# text2 = validate_login(text)
# if len(text2) == 0:
#     print("Пароль не прошёл проверку на соответствие!")
# else:
#     print(text2)

# print("\nЗадание №15")
# # Задание №15
#
#
# def recurs(lst1):
#     count = 0   # Счётчик
#     if len(lst1) == 0:  # Базовый случай!
#         return 0
#     else:
#         if lst1[0] < 0:
#             count += 1
#         return count + recurs(lst1[1:])  # Рекурсивный вызов
#
#
# try:
#     n = int(input("Введите количество чисел в списке: "))
#     lst = [int(input("-> ")) for i in range(0, n)]
#     print(lst)
#     print("Количество отрицательных чисел: ", recurs(lst))
# except TypeError:
#     print("Ошибка! Не число!")


print("\nЗадание №16")
# Задание №16

f = open("revers.txt", "w")  # Создание файла
f.write("Тест:\nЗамена строки в текстовом файла;\nизменить строку в списке;\nзаписать список в файл;\n")
f.close()

# print("Тест:\nЗамена строки в текстовом файла;\nизменить строку в списке;\nзаписать список в файл;\n\n")


f = open("revers.txt", "r")  # Режим чтения файла
read_file = f.readlines()  # Представление в виде списка!
print("Индексы начинаются с 0-го!", read_file)
pos1 = int(input("Индекс заменяющей строки: "))
pos2 = int(input("Индекс заменяемой строки: "))
read_file[pos1], read_file[pos2] = read_file[pos2], read_file[pos1]  # Перестановка строк
f.close()

f = open("revers.txt", "w")  # Стереть предыдущие данные! Для изменения
f.writelines(read_file)
f.close()

