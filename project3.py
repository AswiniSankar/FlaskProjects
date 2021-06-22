from flask import Flask, render_template
app = Flask(__name__)

@app.route('/html')
def index():
    return '<html><body><h1> HELLO WORLD</h1></body></html>'

if __name__ == '__main__':
       app.run(port=5662, debug=True)