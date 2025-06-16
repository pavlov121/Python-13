import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):  # url - страница, path - куда сохранять
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        tems = self.html.find_all("a", class_="similarReadDropdownItem")  # Пункты
        for item in tems:
            descript = item.find("div", class_="gfg-similar-read-item-subheading").text.strip()  # Описание к пунктам
            print("Пункт сайта: ", descript, "\n")
            print("=" * 50)
            self.res.append({
                'desc': descript
            })
        # print(self.res)

    def save(self):
        with open(self.path, "w") as f:
            i = 1
            for item in self.res:
                try:
                    f.write(f"Пункт №{i}\n\nНазвание:{item['desc']}\n")
                    i += 1
                except UnicodeEncodeError:
                    raise "Возьмите другие данные!"

    def run(self):
        self.get_html()
        self.parsing()
        # self.save()  # Для сохранения!
