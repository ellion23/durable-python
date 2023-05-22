import sqlite3
import os
from flask import Flask, render_template, request, g
from FDataBase import FDataBase

database = '/db_base.db'
debug = True
secret_key = 'NotYourDeal'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(database=os.path.join(app.root_path, 'db_base.db')))

def connect_db():
    conn = sqlite3.connect(app.config['database'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    """Соединение с БД, если не установлено"""
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu = dbase.getMenu())


@app.teardown_appcontext
def close_db(error):
    """Закрываем соединение с БД, если оно было установлено"""
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)