from flask import Flask, render_template, url_for, request, flash, session, redirect


def test():
    if len(request.form['username']) > 2:
        return True
    return False

menu = [{'name': 'Главная страница', 'url': ''},
        {'name': 'Типы', 'url': 'kinds'},
        {'name': 'Обратная связь', 'url': 'contact'}]
app = Flask(__name__)
app.config['SECRET_KEY'] = 'A5ks3Z92'


@app.route('/')
def index():
    return render_template("base_after_base.html",
                           title="Главная.",
                           menu=menu)


@app.route('/kinds')
def index_2():
    return render_template("kinds.html",
                           title="О нас.", menu=menu)


@app.route('/contact', methods=["POST", 'GET'])
def contact():
    if request.method == 'POST':
        if test():
            flash('Message sent', category='success')
        else:
            flash('Error', category='error')
        print(request.form)
        print(request.form['username'])
    return render_template('contact.html', title='Обратная связь.', menu=menu)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Ошибка 404.', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
