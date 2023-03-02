from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/hello')
def index():
    return "hellah world"

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    suma = a + b
    return f"La suma es: {str(suma)}"