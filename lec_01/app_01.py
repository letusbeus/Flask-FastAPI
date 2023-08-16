from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
    # return 42 выведет ошибку, т.к. flask может выводить только строковые значения


if __name__ == '__main__':
    app.run()
