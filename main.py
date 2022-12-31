from flask import Flask, request

app = Flask (__name__)

@app.route("/hola/<saludo>", methods= ["POST"])

#saludo entra como parametro dentro de la funcion... en postman
#POST htpps...../hola/holi, 
#                     este es el (saludo)

def hola (saludo):
    data = request.get_json()
    return (saludo+ data["nombre"])

app.run('0.0.0.0')


#en la terminal python main.py-------------> haces correr el servidor
