from flask import Flask, render_template, request, redirect, url_for
from database import Inventario
import json
import csv
import os

app = Flask(__name__)
db_tienda = Inventario()

# --- CONFIGURACIÓN DE RUTAS DE ARCHIVOS ---
# Esto asegura que las carpetas existan para evitar errores
RUTA_CARPETA = 'inventario/data'
if not os.path.exists(RUTA_CARPETA):
    os.makedirs(RUTA_CARPETA)

ARCH_TXT = os.path.join(RUTA_CARPETA, 'datos.txt')
ARCH_CSV = os.path.join(RUTA_CARPETA, 'datos.csv')
ARCH_JSON = os.path.join(RUTA_CARPETA, 'datos.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/celulares')
def listar():
    # Obtiene los datos de la Base de Datos (SQLAlchemy/SQLite)
    equipos = db_tienda.obtener_todo()
    return render_template('celulares.html', equipos=equipos)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_equipo():
    if request.method == 'POST':
        marca = request.form['marca']
        nombre = request.form['nombre']
        cantidad = int(request.form['cantidad'])
        precio = float(request.form['precio'])
        
        # 1. GUARDAR EN BASE DE DATOS (Lo que ya tenías)
        db_tienda.agregar(nombre, marca, cantidad, precio)

        # 2. GUARDAR EN TXT (Semana 12)
        with open(ARCH_TXT, 'a') as f:
            f.write(f"Marca: {marca}, Modelo: {nombre}, Cantidad: {cantidad}, Precio: {precio}\n")

        # 3. GUARDAR EN CSV (Semana 12)
        with open(ARCH_CSV, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([marca, nombre, cantidad, precio])

        # 4. GUARDAR EN JSON (Semana 12)
        nuevo_item = {"marca": marca, "nombre": nombre, "cantidad": cantidad, "precio": precio}
        # Leemos lo que hay, agregamos el nuevo y guardamos
        datos_json = []
        if os.path.exists(ARCH_JSON) and os.path.getsize(ARCH_JSON) > 0:
            with open(ARCH_JSON, 'r') as f:
                try:
                    datos_json = json.load(f)
                except json.JSONDecodeError:
                    datos_json = []
        
        datos_json.append(nuevo_item)
        with open(ARCH_JSON, 'w') as f:
            json.dump(datos_json, f, indent=4)

        return redirect(url_for('listar'))
    
    return render_template('formulario.html')

# NUEVA RUTA: Para mostrar los datos de los archivos (Punto 2.2)
@app.route('/ver_archivos')
def ver_archivos():
    contenido_txt = []
    if os.path.exists(ARCH_TXT):
        with open(ARCH_TXT, 'r') as f:
            contenido_txt = f.readlines()
            
    return render_template('datos.html', lista=contenido_txt)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    db_tienda.eliminar(id)
    return redirect(url_for('listar'))

if __name__ == '__main__':
    app.run(debug=True)