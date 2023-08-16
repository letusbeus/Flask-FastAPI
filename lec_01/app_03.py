from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/Фёдор')
@app.route('/Федя')
@app.route('/Федор')
@app.route('/Fedor')
def fedor():
    return 'Привет, Феодор!'


if __name__ == '__main__':
    app.run(debug=True)
