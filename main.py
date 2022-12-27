from flask import Flask, request

app = Flask (__name__)

@app.route("/hola/<saludo>", methods= ["POST"])

def hola (saludo):
    data = request.get_json()
    return (saludo+ data["nombre"])

app.run('0.0.0.0')

