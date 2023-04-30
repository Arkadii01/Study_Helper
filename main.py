from flask import Flask, render_template, request, url_for
from docx_writing import parsing_save, summ_docx
#from pres_writing import *
from flask_dropzone import Dropzone
from flask_bootstrap import Bootstrap
import webbrowser
import sqlite3
from random import choice
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.update(
    UPLOADED_PATH = os.path.join(basedir, 'uploads'),
    DROPZONE_MAX_FILE_SIZE = 1024,
    DROPZONE_TIMEOUT = 5*6*1000)
bootstrap = Bootstrap(app)

@app.route('/')
def sign_in_showing():
    return render_template('sign_in.html')

@app.route('/', methods=['POST'])
def sign_in_doing():
    global email
    email = request.form['email']
    password = request.form['password']
    need_password = request.form['need_password']
    if password == need_password:
        return render_template('about_us.html', color = color, lighting = lighting)
    return render_template('sign_in.html', need_passwordin = need_password, passwordin = password)


@app.route('/aboutus')
def about_us_showing():
    return render_template('about_us.html', color = color, lighting = lighting)


@app.route('/doc')
def into_doc_showing():
    search = ''
    doc_name = ''
    links = ''
    return render_template('doc.html', color = color, lighting = lighting, search = search, doc_name = doc_name, links = links)

@app.route('/doc', methods=['POST', 'GET'])
def into_doc_doing():
    search = request.form['search']
    if search != '':
        webbrowser.open(f'https://yandex.ru/search/?text={"+".join(search.split())}&lr=62')
        webbrowser.open(f'www.google.ru/search?q={"+".join(search.split())}')
    doc_name = request.form['doc_name']
    links = request.form['links'].split('\n')
    if links != []:
        parsing_save(doc_name, links)
    return render_template('doc.html', color = color, lighting = lighting, search = search, doc_name = doc_name, links = links)


@app.route('/recom')
def recom_showing():
    help = ''
    return render_template('recom.html', color = color, lighting = lighting, help = help)

@app.route('/recom', methods=['POST', 'GET'])
def recom_doing():
    help = ''
    with open('recomendations.txt', 'r') as file:
        helps = file.readlines()
    print(123)
    help = choice(helps)
    return render_template('recom.html', help = help, color = color, lighting = lighting)

@app.route('/into_text')
def into_text_showing():
    return render_template('into_text.html', color = color, lighting = lighting)

@app.route('/settings')
def settings_showing():
    return render_template('settings.html', color = color, lighting = lighting)

@app.route('/settings', methods=['POST', 'GET'])
def settings_doing():
    color = request.form["color"]
    lighting = request.form['lighting']
    return render_template('settings.html', color = color, lighting = lighting)

@app.route('/timetable')
def timetable_showing():
    return render_template('timetable.html', color = color, lighting = lighting)


if __name__ == '__main__':
    email = ''
    lighting = 'light'
    color = 'green'
    app.run(port=8080, host='127.0.0.1')