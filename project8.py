from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    dict = {'phy':50,'maths':90,'chm':70,'bio':66}
    return render_template('table.html',result = dict)


if __name__ == '__main__':
    app.run(port=5004, debug=True)
