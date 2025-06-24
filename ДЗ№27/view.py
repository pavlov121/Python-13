def add_title(title):
    def wrapper(fn):
        def wrap(*args, **kwargs):
            print(f"{title}".center(7, "="))
            output = fn(*args, **kwargs)
            print("=" * 20)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title("Редактировать данные каталога фильмов: ")
    def wait_user_answer(self):  # Вывод основного экрана
        print(f"Действия с фильмами:\n"
              f"1 - добавление фильма\n"
              f"2 - каталог фильмов\n"
              f"3 - просмотр определённого фильма\n"
              f"4 - удаление фильма\n"
              f"q - выход из программы!")
        answer = input("Выберите вариант действия: ")
        return answer

    @add_title("Добавление фильма: ")
    def add_user_film(self):  # Добавление фильма
        dict_film = {
            "название": None,
            "жанр": None,
            "режиссёр": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актёры": None
        }
        for key in dict_film:
            dict_film[key] = input(f"Введите пожалуйста {key} фильма: ")

        return dict_film

    @add_title("Каталог фильмов: ")
    def show_all_films(self, films):  # Каталог фильмов
        for ind, film in enumerate(films, 1):  # Начиная с первого фильма!
            print(f"{ind}.{film}")

    @add_title("Ввод названия фильма: ")
    def get_about_film(self):
        return input("Введите название фильма(title): ")

    @add_title("Просмотр фильма")
    def show_film(self, film):
        for key in film:
            print(f"{key} фильма - {film[key]}")  # Вывод каждого значения определённого фильма

    @add_title("Сообщение об ошибке!!!")
    def show_incorrect(self, n):
        print(f"Статья с названием {n} не существует!")

    @add_title("Удаление фильма :")
    def before_del(self):
        return input("Введите название фильма, который хотите удалить(title): ")

    @add_title("Неудачное удаление!")
    def show_del(self, film):
        print(f"Фильм с названием: {film} - не существует!")

    @add_title("Удаление было успешно завершено!")
    def after_del(self, f):
        print(f"Фильм {f} был удалён!")
