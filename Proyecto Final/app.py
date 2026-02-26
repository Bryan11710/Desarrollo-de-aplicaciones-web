from flask import Flask, render_template, request, redirect, url_for
from database import Inventario

app = Flask(__name__)
db_tienda = Inventario()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/celulares')
def listar():
    # Corregido: 'obtener_todo' coincide con database.py
    equipos = db_tienda.obtener_todo()
    return render_template('celulares.html', equipos=equipos)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_equipo():
    if request.method == 'POST':
        marca = request.form['marca']
        nombre = request.form['nombre']
        cantidad = int(request.form['cantidad'])
        precio = float(request.form['precio'])
        # Corregido: 'agregar' coincide con database.py
        db_tienda.agregar(nombre, marca, cantidad, precio)
        return redirect(url_for('listar'))
    return render_template('formulario.html')

@app.route('/eliminar/<int:id>')
def eliminar(id):
    db_tienda.eliminar(id)
    return redirect(url_for('listar'))

if __name__ == '__main__':
    app.run(debug=True)