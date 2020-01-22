# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations.add(a,b)
    
    return f'a + b = {result}'

@app.route('/sub')
def sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations.sub(a,b)

    return f'a - b = {result}'

@app.route('/mult')
def mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations.mult(a,b)

    return f'a * b = {result}'

@app.route('/div')
def div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations.div(a,b)

    return f'a / b = {result}'

@app.route('/math/<operation>')
def do_math(operation):
    math_functions = {
        "add": operations.add,
        "sub": operations.sub,
        "mult": operations.mult,
        "div": operations.div
    }

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    result = math_functions[operation]

    return f'what is math anyway: {result(a,b)}'