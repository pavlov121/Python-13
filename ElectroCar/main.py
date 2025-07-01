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
from dataclasses import field
from fileinput import filename

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


# print("\nЗадание №16")
# # Задание №16
#
# f = open("revers.txt", "w")  # Создание файла
# f.write("Тест:\nЗамена строки в текстовом файла;\nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()
#
# # print("Тест:\nЗамена строки в текстовом файла;\nизменить строку в списке;\nзаписать список в файл;\n\n")
#
#
# f = open("revers.txt", "r")  # Режим чтения файла
# read_file = f.readlines()  # Представление в виде списка!
# print("Индексы начинаются с 0-го!", read_file)
# pos1 = int(input("Индекс заменяющей строки: "))
# pos2 = int(input("Индекс заменяемой строки: "))
# read_file[pos1], read_file[pos2] = read_file[pos2], read_file[pos1]  # Перестановка строк
# f.close()
#
# f = open("revers.txt", "w")  # Стереть предыдущие данные! Для изменения
# f.writelines(read_file)
# f.close()

# print("\nЗадание №17")
# # Задание №17
#
#
# class Car:
#
#     def __init__(self, model, year, author, power, color, price):  # Создание и инициализация закрытых свойств
#         self.__model = model
#         self.__year = year
#         self.__author = author
#         self.__power = power
#         self.__color = color
#         self.__price = price
#
#     @property  # геттер для закрытого свойства model! (Получить значение)
#     def model(self):
#         return self.__model
#
#     @model.setter  # сеттер для закрытого свойства model! (Установить значение)
#     def model(self, model1):
#         if isinstance(model1, str):
#             self.__model = model1
#         else:
#             print("Введите строку!")
#
#     @property  # геттер для закрытого свойства year! (Получить значение)
#     def year(self):
#         return self.__year
#
#     @year.setter  # сеттер для закрытого свойства year! (Установить значение)
#     def year(self,  year1):
#         if isinstance(year1, int):
#             self.__year = year1
#         else:
#             print("Введите число!")
#
#     @property  # геттер для закрытого свойства author! (Получить значение)
#     def author(self):
#         return self.__model
#
#     @author.setter  # сеттер для закрытого свойства author! (Установить значение)
#     def author(self, author1):
#         if isinstance(author1, str):
#             self.__author = author1
#         else:
#             print("Введите строку!")
#
#     @property  # геттер для закрытого свойства power! (Получить значение)
#     def power(self):
#         return self.__power
#
#     @power.setter  # сеттер для закрытого свойства power! (Установить значение)
#     def power(self, power1):
#         if isinstance(power1, int):
#             self.__power = power1
#         else:
#             print("Введите число!")
#
#     @property  # геттер для закрытого свойства color! (Получить значение)
#     def color(self):
#         return self.__color
#
#     @color.setter  # сеттер для закрытого свойства color! (Установить значение)
#     def color(self, color1):
#         if isinstance(color1, str):
#             self.__color = color1
#         else:
#             print("Введите строку!")
#
#     @property  # геттер для закрытого свойства price! (Получить значение)
#     def price(self):
#         return self.__price
#
#     @price.setter  # сеттер для закрытого свойства price! (Установить значение)
#     def price(self, price1):
#         if isinstance(price1, int):
#             self.__price = price1
#         else:
#             print("Введите число!")
#
#     def print_info(self):  # Вывод структурной информации на экран
#         print("Данные автомобиля".center(40, "*"))
#         print(f"Название модели: {self.__model}\nГод выпуска: {self.__year}\nПроизводитель: {self.__author}"
#               f"\nМощность двигателя: {self.__power} л.с.\nЦвет машины: {self.__color}\nЦена: {self.__price}")
#         print("=" * 40)
#
#
# car1 = Car("X7 M50i", 2021, "BMW", 530, "white", 10790000)
# car1.print_info()
# car1.model = "ВАЗ 2106"
# car1.year = 2024
# car1.author = "Lada"
# car1.power = 200000
# car1.color = "black"
# car1.price = 120000
# car1.print_info()

# # print("\nЗадание №18")
# # # Задание №18
# import math
#
#
# class Figure:
#     count = 0  # Счётчик(статическое свойство)
#
#     def __init__(self, a, b, h):  # Инициализация стороны треугольника, прямоугольника, высоты(динамических свойств)
#         self.__a = a
#         self.__b = b
#         self.__h = h
#
#     @staticmethod
#     def triangle_prim(a, h):  # Площадь прямоугольного треугольника
#         Figure.count += 1
#         print(f"Площадь прямоугольного треугольника ({a}, {h}) = {a * h}")
#
#     @staticmethod
#     def rectangle(a, b):  # Площадь прямоугольника
#         Figure.count += 1
#         print(f"Площадь прямоугольника ({a}, {b}) = {a * b}")
#
#     @staticmethod
#     def square(a):  # Площадь квадрата
#         Figure.count += 1
#         print(f"Площадь квадрата ({a}^2) = {a * a}")
#
#     @staticmethod
#     def shet_def() -> None:
#         print(f"Количество вызовов = {Figure.count}")
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, a):
#         if isinstance(a, int):
#             self.__a = a
#         else:
#             raise TypeError("Ошибка типа!")
#
#     @property
#     def b(self):
#         return self.__a
#
#     @b.setter
#     def b(self, b):
#         if isinstance(b, int):
#             self.__b = b
#         else:
#             raise TypeError("Ошибка типа!")
#
#     @property
#     def h(self):
#         return self.__a
#
#     @h.setter
#     def h(self, h):
#         if isinstance(h, int):
#             self.__h = h
#         else:
#             raise TypeError("Ошибка типа!")
#
#
# a1 = Figure(15, 12, 13)
# a1.rectangle(14, 15)
# a1.triangle_prim(15, 12)
# a1.square(2)
# a1.shet_def()

# Занятие 19
# class Account:
#     rate_usd = 0.013  # Курс рубля по отношению к доллару
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счёт #{self.num} принадлежащий {self.surname} был открыт")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счёт #{self.num} принадлежащий {self.surname} был закрыт")
#
#     @property  # Первый способ!
#     def surname(self):
#         return self.surname
#
#     @surname.setter
#     def surname(self, surname):
#         self.surname = surname
#
#     @property
#     def num(self):
#         return self.num
#
#     @num.setter
#     def num(self, num):
#         self.surname = num
#
#     @property
#     def percent(self):
#         return self.percent
#
#     @percent.setter
#     def percent(self, percent):
#         self.percent = percent
#
#     @property
#     def value(self):
#         return self.value
#
#     @value.setter
#     def value(self, value):
#         self.value = value
#
#     def get_surname(self):  # Второй способ!
#         return self.surname
#
#     def set_surname(self, surname):
#         self.surname = surname
#
#     def get_num(self):  # Второй способ!
#         return self.surname
#
#     def set_num(self, num):
#         self.num = num
#
#     def get_percent(self):  # Второй способ!
#         return self.surname
#
#     def set_percent(self, percent):
#         self.percent = percent
#
#     def get_value(self):  # Второй способ!
#         return self.surname
#
#     def set_value(self, value):
#         self.value = value
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):  # rate - новый курс
#         cls.rate_usd = rate  # Заменяем курс!
#
#     @classmethod
#     def set_eur_rate(cls, rate):  # rate - новый курс
#         cls.rate_eur = rate  # Заменяем курс!
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счёта: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счёта: {eur_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счёте:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)  # Меняем статическое свойство класса Account
# Account.set_eur_rate(3)
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дона")
# acc.print_info()
# print()
#
# acc.add_percent()
# print()
#
# acc.withdraw_money(900)
# print()
#
# acc.withdraw_money(200)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()

# print("\nЗадание №20")
# # # Задание №20


# from abc import ABC, abstractmethod
#
#
# class Human(ABC):
#
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#     @abstractmethod
#     def display3(self):
#         pass
#
#
# class Student(Human):  # Наследование от класса человек!
#
#     def display1(self):
#         print(f"Загидулин Линар 32 РПО PD_011 5\nШугани Сергей 15 РПО PD_011 5 Защита данных")
#
#
# class Teacher(Human):  # Наследование от класса человек!
#
#     def display2(self):
#         print(f"Даньшин Андрей 38 Астрофизика 110\n Башкиров Алексей 45 Разработка приложений 20")
#
#
# class Graduate(Student):  # Наследование от класса студент!
#
#     def display3(self):
#         print(f"Батодалаев Даши 16 ГК Web_011 5\nМаркин Даниил ГК Python_011 5")

# print("\nЗадание №21")
# # # Задание №21
#
# class Student:
#     def __init__(self, name1, name2):
#         self.name1 = name1
#         self.name2 = name2
#         self.m = self.Model()
#         self.p = self.Processor()
#         self.me = self.Memory()
#
#     # @property
#     # def name1(self):
#     #     return self.name1
#     #
#     # @name1.setter
#     # def name1(self, name1):
#     #     if not isinstance(name1, str):
#     #         raise TypeError("Не строка!")
#     #     else:
#     #         self.name1 = name1
#     #
#     # @property
#     # def name2(self):
#     #     return self.name2
#     #
#     # @name2.setter
#     # def name2(self, name2):
#     #     if not isinstance(name2, str):
#     #         raise TypeError("Не строка!")
#     #     else:
#     #         self.name2 = name2
#
#     def __str__(self):
#         print(f"{self.name1} => {self.m}, {self.p}, {self.me}\n"
#               f"{self.name2} => {self.m}, {self.p}, {self.me}")
#
#     def print_info(self):
#         print(f"{self.name1} => {self.m}, {self.p}, {self.me}\n"
#               f"{self.name2} => {self.m}, {self.p}, {self.me}")
#
#     class Model:
#         model = 'HP'
#
#         def __str__(self):
#             return self.model
#
#     class Processor:
#         processor = 'i7'
#
#         def __str__(self):
#             return self.processor
#
#     class Memory:
#         memory = "16"
#
#         def __str__(self):
#             return self.memory
#
#         # @property
#         # def model(self):
#         #     return self.model
#         #
#         # @model.setter
#         # def model(self, model):
#         #     if not isinstance(model, str):
#         #         raise TypeError("Не строка!")
#         #     else:
#         #         self.model = model
#         #
#         # @property
#         # def processor(self):
#         #     return self.model
#         #
#         # @processor.setter
#         # def processor(self, processor):
#         #     if not isinstance(processor, str):
#         #         raise TypeError("Не строка!")
#         #     else:
#         #         self.processor = processor
#         #
#         # @property
#         # def memory(self):
#         #     return self.model
#         #
#         # @memory.setter
#         # def memory(self, memory):
#         #     if not isinstance(memory, str):
#         #         raise TypeError("Не строка!")
#         #     else:
#         #         self.memory = memory  # Через p #
#
#
# one = Student('Лёша', 'Настя')
# one.print_info()

# # Задание 22
#
# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):  # +
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)  # Clock(300)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __sub__(self, other):  # -
#         if not isinstance(other, Clock):
#             raise ValueError("Не целое число!")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):  # -
#         if not isinstance(other, Clock):
#             raise ValueError("Не целое число!")
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):  # //
#         if not isinstance(other, Clock):
#             raise ValueError("Не целое число!")
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):  # %
#         if not isinstance(other, Clock):
#             raise ValueError("Не целое число!")
#         return Clock(self.sec % other.sec)
#
#     def __lt__(self, other):  # <
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec > other.sec
#
#     def __le__(self, other):  # <=
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec <= other.sec
#
#     def __gt__(self, other):  # >
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec > other.sec
#
#     def __ge__(self, other):  # <
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec >= other.sec
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# # c4 = Clock(300)
# # c3 = c1 + c2 + c4
# print(c1.get_format_time())
# print(c2.get_format_time())
# # c1 += c2
# # print(c1.get_format_time())
# # print(c2.get_format_time())
# # print(c4.get_format_time())
# # print(c3.get_format_time())
# if c1 != c2:
#     print("Время разное")
# else:
#     print("Время одинаковое")

# # Занятие 23
#
#
# from ElectroCar import Car
#
#
# # Дочерний класс
#
# class ElCar(Car.Car):
#     pass
#
#
# car1 = ElCar("Tesla", "T", "2018", "99000", "100")
# print(car1.info())

# # Занятие 24
#
# import json
# from random import choice  # Выбор одного элемента из списка
#
#
# def gen_person():
#     name = ' '
#     tel = ' '
#
#     letters = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'k', 'l', 'm', 'n']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(num)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
#
# def func():  # Функция создание рандомного ключа
#     num1 = ' '
#     num2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#     while len(num1) != 14:
#         num1 += choice(num2)
#     return num1
#
#
# def write_json(person_dict):  # Добавление словарей в словарь
#     try:
#         data = json.load(open('person.json'))  # Откроет + считает файл
#     except FileNotFoundError:
#         data = {}
#
#     data.update({func(): person_dict})  # Добавление на один словарь
#     with open('person.json', 'w') as f:
#         json.dump(data, f, indent=6)
#
#
# # lst = {func(): gen_person() for i in range(5)}
# # for i in range(5):
# #     print(gen_person())
# for i in range(5):
#     write_json(gen_person())

# # Занятие 25
#
# import requests
# import json
# import csv
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")  # На получение файла
# todos = json.loads(response.text)
# print(todos)
#
# dict_values = []
# for i in todos:
#     dict_values.append(i.values())
# print(dict_values)
# a = []
# for row in todos:
#     b = list(row.values())
#     a.append(b)
#
# print(a)
# with open("ДЗ25.csv", "w") as f:  # Создание и запись данных в формате csv
#     # shapka = ["userId", "id", "title", "completed"]
#     write = csv.writer(f, delimiter=";", lineterminator="\r")
#     for i in a:
#         write.writerow(i)
#     write.writerows(a)

# # Занятие 26
#
# from parser import Parser
#
#
# def main():
#     pars = Parser("https://www.geeksforgeeks.org/python/convert-csv-to-excel-using-pandas-in-python/", "My.txt")
#     pars.run()
#
#
# if __name__ == "__main__":
#     main()

# Занятие 30
import sqlite3

with sqlite3.connect("education.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT NOT NULL,
    name TEXT NOT NULL,
    patronymic TEXT NOT NULL,
    age INTEGER NOT NULL CHECK(age >= 17 AND age < 50),
    [group] TEXT NOT NULL,
    FOREIGN KEY ([group]) REFERENCES groups(id) ON DELETE RESTRICT
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS groups(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT NOT NULL
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS lessons(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        e TEXT NOT NULL
        )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS association(
        group_id INTEGER,
        lesson_id INTEGER,
        PRIMARY KEY (group_id, lesson_id)
        FOREIGN KEY (group_id) REFERENCES groups(id)
        FOREIGN KEY (lesson_id) REFERENCES lessons(id)
       ) """)
