from flask import Flask, request

app = Flask(__name__)


@app.route('/python')
def hello():
    return "Hello earth!"


@app.route('/main/')
def main():
    return "main program"


if __name__ == '__main__':
    app.run(debug=True)
