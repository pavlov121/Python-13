from view import UserInterface
from model import FilmModel


class Controller:
    def __init__(self):
        self.film_model = FilmModel()
        self.user_interface = UserInterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            film = self.user_interface.add_user_film()
            self.film_model.add_film(film)
        if answer == "2":
            film = self.film_model.get_all_films()
            self.user_interface.show_all_films(film)
        if answer == "3":
            see_film = self.user_interface.get_about_film()
            try:
                film = self.film_model.get_about(see_film)
            except KeyError:
                self.user_interface.show_incorrect(see_film)
            else:
                self.user_interface.show_film(film)
        if answer == "4":
            del_film = self.user_interface.before_del()
            try:
                film = self.film_model.del_film(del_film)
            except KeyError:
                self.user_interface.show_del(del_film)
            else:
                self.user_interface.after_del(film)



