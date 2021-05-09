from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/app')
def blog():
    return "Hello, from App!"



if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8081)