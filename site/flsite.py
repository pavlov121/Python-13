from http.cookiejar import debug
from flask import Flask, render_template

app = Flask(__name__)

menu = [
    {'name': "Главная страница", 'url': "index"},
    {'name': "Помощь", 'url': "help"},
    {'name': "Об авторе", 'url': "author"}
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Главная", menu=menu)


@app.route("/help")
def help():
    return render_template("help.html", title="Помощь", menu=menu)


@app.route("/author")
def author():
    return render_template("author.html", title="Автор", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
