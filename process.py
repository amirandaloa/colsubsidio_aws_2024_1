from flask import Flask, render_template, request
import requests
import json
from models import Modelo
from main import app
import boto3
import os







# Configuración de AWS S3
S3_BUCKET_NAME = 'curso-aws-colsub'
S3_ACCESS_KEY = ''
S3_SECRET_KEY = ''

s3 = boto3.client(
    's3',
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY
)

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            try:
                s3.upload_fileobj(
                    file,
                    S3_BUCKET_NAME,
                    file.filename,
                    ExtraArgs={'ACL': 'public-read'}
                )
                return 'Imagen subida correctamente a AWS S3.'
            except Exception as e:
                return str(e)
    return 'Error al subir la imagen.'


@app.route("/", methods=["GET"])
def index():
    return render_template("loader.html")



@app.route("/consultar", methods=["GET"])
def consultar_producto():
    #nombre = request.args.get("nombre")
    producto = obtener_producto()

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


def obtener_producto():
    try:
        modelo = Modelo()
        modelo.execute_query('select * from darek_sch.d_users')
        return None
    except FileNotFoundError:
        return None