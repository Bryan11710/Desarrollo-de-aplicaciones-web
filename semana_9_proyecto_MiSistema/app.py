from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bienvenido a Mi Sistema de Gestión</h1><p>Backend operativo en Flask - Semana 9.</p>"

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f"<h1>Hola, {nombre}</h1><p>Acceso concedido al sistema.</p>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)