from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from Conexion.conexion import obtener_conexion
import os

app = Flask(__name__)
app.secret_key = 'clave_secreta_technova_2026' # Necesaria para manejar sesiones

# --- CONFIGURACIÓN DE FLASK-LOGIN ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Redirige aquí si no hay sesión activa

# Modelo de Usuario para Flask-Login
class Usuario(UserMixin):
    def __init__(self, id, nombre, mail):
        self.id = id
        self.nombre = nombre
        self.mail = mail

@login_manager.user_loader
def load_user(user_id):
    db = obtener_conexion()
    if db:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        db.close()
        if user_data:
            return Usuario(user_data['id_usuario'], user_data['nombre'], user_data['mail'])
    return None

# --- RUTA DE LOGIN (NUEVO) ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        db = obtener_conexion()
        if db:
            cursor = db.cursor(dictionary=True)
            # Buscamos al usuario por mail y password (como en la semana 13)
            cursor.execute("SELECT * FROM usuarios WHERE mail = %s AND password = %s", (email, password))
            user_data = cursor.fetchone()
            cursor.close()
            db.close()

            if user_data:
                user_obj = Usuario(user_data['id_usuario'], user_data['nombre'], user_data['mail'])
                login_user(user_obj)
                return redirect(url_for('listar'))
            else:
                flash('Credenciales incorrectas. Intenta de nuevo.')
    
    return render_template('login.html')

# --- RUTA DE LOGOUT (NUEVO) ---
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# --- RUTA DE INICIO ---
@app.route('/')
def index():
    return render_template('index.html')

# --- LISTAR EQUIPOS (Protegido) ---
@app.route('/celulares')
@login_required
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

# --- AGREGAR EQUIPO (Protegido) ---
@app.route('/agregar', methods=['GET', 'POST'])
@login_required
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

# --- ELIMINAR EQUIPO (Protegido) ---
@app.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    db = obtener_conexion()
    if db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM equipos WHERE id = %s", (id,))
        db.commit()
        cursor.close()
        db.close()
    return redirect(url_for('listar'))

# --- REGISTRO DE USUARIOS (Sigue siendo público para poder crear el primer usuario) ---
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