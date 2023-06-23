from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)

menu = [
    {'name': "Главное меню", 'url': "main_menu"},
    {'name': "Ферма", 'url': "farm"},
    {'name': "Работники", 'url': "profile"}
]


@app.route("/")
@app.route("/main_menu")
def main_menu():
    print(url_for('main_menu'))
    return render_template('mainmenu.html', title='Главное меню', menu=menu)


@app.route("/profile")
def profile():
    print(url_for('profile'))
    return render_template('profile.html', title='Работники', menu=menu)


@app.route("/farm")
def farm():
    print(url_for('farm'))
    return render_template('farm.html', title='Ферма', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
