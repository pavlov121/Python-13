# Родительский класс
# Дескриптор
class ValidString:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.__name} должно быть строкой")
        instance.__dict__[self.__name] = value


class Car:
    brand = ValidString()
    model = ValidString()
    year = ValidString()
    beg = ValidString()
    power = ValidString()

    def __init__(self, brand, model, year, beg, power):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__beg = beg
        self.__power = power

    def info(self):
        return (f"{self.__brand}, {self.__model}, {self.__year} год, {self.__beg} км\n"
                f"Этот автомобиль имеет мощность {self.__power} %")
