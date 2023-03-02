from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    suma = a + b
    return f"La suma es: {str(suma)}"