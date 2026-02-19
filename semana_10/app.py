from flask import Flask, render_template

app = Flask(__name__)

# 1. RUTA PRINCIPAL (INDEX)
@app.route('/')
def index():
    # Ya no retorna texto plano, renderiza el HTML
    return render_template('index.html')

# 2. RUTA "ACERCA DE" (ABOUT)
@app.route('/about')
def about():
    return render_template('about.html')

# 3. RUTA ADICIONAL: CATÁLOGO DE CELULARES
@app.route('/celulares')
def celulares():
    # Lista de diccionarios que simula una base de datos de productos
    catalogo_celulares = [
        {"marca": "Apple", "modelo": "iPhone 15 Pro", "precio": 999, "color": "Titanio"},
        {"marca": "Samsung", "modelo": "Galaxy S24 Ultra", "precio": 1199, "color": "Negro"},
        {"marca": "Xiaomi", "modelo": "Redmi Note 13", "precio": 299, "color": "Azul"},
        {"marca": "Google", "modelo": "Pixel 8", "precio": 699, "color": "Obsidiana"},
        {"marca": "Motorola", "modelo": "Edge 40", "precio": 450, "color": "Verde"}
    ]
    # Pasamos la lista a la plantilla bajo el nombre 'equipos'
    return render_template('celulares.html', equipos=catalogo_celulares)

# 4. RUTA ADICIONAL: CONTACTO (Opcional para dar más volumen al proyecto)
@app.route('/contacto')
def contacto():
    return "<h3>Página de contacto en construcción...</h3><a href='/'>Volver</a>"

if __name__ == '__main__':
    # Ejecuta el servidor en modo desarrollo
    app.run(debug=True)