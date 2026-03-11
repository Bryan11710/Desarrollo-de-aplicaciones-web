from flask import Flask, render_template, request, redirect, url_for
from Conexion.conexion import obtener_conexion
import os

app = Flask(__name__)

# --- RUTA DE INICIO ---
@app.route('/')
def index():
    return render_template('index.html')

# --- LISTAR EQUIPOS (Consultar MySQL) ---
@app.route('/celulares')
def listar():
    db = obtener_conexion()
    if db:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM equipos")
        equipos = cursor.fetchall()
        cursor.close()
        db.close()
        return render_template('celulares.html', equipos=equipos)
    return "Error al conectar con la base de datos."

# --- AGREGAR EQUIPO (Insertar en MySQL) ---
@app.route('/agregar', methods=['GET', 'POST'])
def agregar_equipo():
    if request.method == 'POST':
        marca = request.form['marca']
        nombre = request.form['nombre']
        cantidad = int(request.form['cantidad'])
        precio = float(request.form['precio'])
        
        db = obtener_conexion()
        if db:
            cursor = db.cursor()
            sql = "INSERT INTO equipos (marca, nombre, cantidad, precio) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (marca, nombre, cantidad, precio))
            db.commit()
            cursor.close()
            db.close()
            return redirect(url_for('listar'))
    
    return render_template('formulario.html')

# --- ELIMINAR EQUIPO ---
@app.route('/eliminar/<int:id>')
def eliminar(id):
    db = obtener_conexion()
    if db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM equipos WHERE id = %s", (id,))
        db.commit()
        cursor.close()
        db.close()
    return redirect(url_for('listar'))

# --- REGISTRO DE USUARIOS (Requisito Semana 13) ---
@app.route('/usuarios', methods=['GET', 'POST'])
def gestionar_usuarios():
    db = obtener_conexion()
    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        nombre = request.form['nombre']
        mail = request.form['mail']
        password = request.form['password']
        
        cursor.execute("INSERT INTO usuarios (nombre, mail, password) VALUES (%s, %s, %s)", (nombre, mail, password))
        db.commit()
        return redirect(url_for('gestionar_usuarios'))

    cursor.execute("SELECT * FROM usuarios")
    lista_usuarios = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('usuarios.html', usuarios=lista_usuarios)

if __name__ == '__main__':
    app.run(debug=True)