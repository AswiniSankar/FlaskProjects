from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/<int:score>')
def hello_score(score):
    return render_template('hello.html', marks=score)


if __name__ == '__main__':
    app.run(port=5002, debug=True)
