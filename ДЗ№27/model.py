class Film:  # Один фильм
    def __init__(self, title, gan, author, year, long, stud, arty):
        self.title = title
        self.gan = gan
        self.author = author
        self.year = year
        self.long = long
        self.stud = stud
        self.arty = arty

    def __str__(self):
        return f"Фильм: {self.title}, от режиссёра {self.author}"


class FilmModel:  # Каталог фильмов
    def __init__(self):
        self.films = {}

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[film.title] = film

    def get_all_films(self):
        return self.films.values()

    def get_about(self, user_film):  # Просмотр определённого фильма
        film = self.films[user_film]
        dict_film = {
            "название фильма": film.title,
            "жанр": film.gan,
            "режиссёр": film.author,
            "год выпуска": film.year,
            "длительность": film.long,
            "студия": film.stud,
            "актёры": film.arty
        }
        return dict_film

    def del_film(self, user_film):
        del self.films[user_film]
        print(f"Фильм {user_film} удалён!")


