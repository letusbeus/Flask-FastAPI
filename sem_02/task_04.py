"""
Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить", при нажатии на которую будет произведен подсчет количества слов в тексте и переход на страницу с результатом.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/name/')
def name_page():
    name1 = 'user'
    return render_template('greetings.html', name=name1)


@app.route('/pic/')
def pic_page():
    return render_template('pic.html')


@app.route('/upload/')
def upload_page():
    return render_template('upload.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    user_login = 'qwerty'
    user_pwd = '123'
    if request.method == 'POST':
        log = request.form['login']
        pas = request.form['password']
        print(log, pas)
        if log == user_login and pas == user_pwd:
            return render_template('greetings.html', name = log)
        else:
            return render_template('error.html')
    return render_template('login.html')


@app.route('/message/', methods=['GET', 'POST'])
def message_page():
    if request.method == 'POST':
        message = request.form['messsage_python']
        number_of_words = len([word for word in message.split()])
        return render_template('message_result.html', number_of_words=number_of_words)
    return render_template('send.html')


if __name__ == '__main__':
    app.run(debug=True)
