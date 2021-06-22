from flask import Flask

app = Flask(__name__)


@app.route('/stringvalue/<name>')
def hello_name(name):
    return "Hello %s!!" % name


@app.route('/integervalue/<int:age>')
def hello_age(age):
    return "your age is %d" % age


@app.route('/floatvalue/<float:height>')
def hello_heigt(height):
    return "your height is %f" % height


if __name__ == '__main__':
    app.run(port=5001,debug=True)
