from flask import Flask, render_template, url_for, request, flash, session, redirect


def test():
    if len(request.form['username']) > 2:
        return True
    return False


menu = [{'name': 'Главная страница', 'url': 'index'},
        {'name': 'О сайте', 'url': 'about'},
        {'name': 'Обратная связь', 'url': 'contact'}]
app = Flask(__name__)
app.config['SECRET_KEY'] = 'kept_waiting'


@app.route('/index')
def index():
    return render_template("base_after_base.html",
                           title = "ГОРШОК",
                           menu = menu)


@app.route('/about')
def index_2():
    return render_template("index.html",
                           title = "ЦОЙ", menu=menu)


@app.route('/contact', methods=["POST", 'GET'])
def contact():
    if request.method == 'POST':
        if test():
            flash('Message sent', category='success')
        else:
            flash('Error', category='error')
        print(request.form)
        print(request.form['username'])
    return render_template('contact.html', title='Обратная связь', menu=menu)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='слыш.', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
