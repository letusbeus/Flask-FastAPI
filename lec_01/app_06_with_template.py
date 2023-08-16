from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/index/')
def html_index():
    return render_template('index1.html')


@app.route('/home/')
def html_home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
