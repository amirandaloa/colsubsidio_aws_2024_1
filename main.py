from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")



@app.route("/consultar", methods=["GET"])
def consultar_producto():
    nombre = request.args.get("nombre")
    producto = obtener_producto_por_nombre(nombre)

    if producto:
        return render_template("resultado.html", producto=producto)
    else:
        return render_template("error.html", mensaje="Producto no encontrado")

@app.route("/editar", methods=["POST"])
def editar_producto():
    try:
        nombre= request.form.get("nombre")
        nuevo_precio= request.form.get("precio")
        with open('productos.json', 'r+') as json_file:
            data = json.load(json_file)
            for producto in data:
                if producto['nombre'] == nombre:
                    producto['precio'] = nuevo_precio
                    json_file.seek(0)  # Reiniciar el puntero al principio del archivo
                    json.dump(data, json_file, indent=4)
                    json_file.truncate()  # Truncar el archivo para eliminar los datos restantes
                    return render_template("resultado.html", producto=producto)
        return False
    except FileNotFoundError:
        return False


def obtener_producto_por_nombre(nombre):
    try:
        with open('productos.json') as json_file:
            data = json.load(json_file)
            for producto in data:
                if producto['nombre'] == nombre:
                    return {"nombre": producto['nombre'], "precio": producto['precio']}
        return None
    except FileNotFoundError:
        return None


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)