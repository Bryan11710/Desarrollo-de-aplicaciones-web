import sqlite3
from models import Celular

class Inventario:
    def __init__(self):
        self.db = "celustore.db"
        self._crear_tabla()

    def conectar(self):
        return sqlite3.connect(self.db)

    def _crear_tabla(self):
        with self.conectar() as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS productos 
                         (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                          nombre TEXT, marca TEXT, cantidad INTEGER, precio REAL)''')

    def agregar(self, n, m, c, p):
        """Método para insertar datos"""
        with self.conectar() as conn:
            conn.execute("INSERT INTO productos (nombre, marca, cantidad, precio) VALUES (?,?,?,?)", (n, m, c, p))

    def obtener_todo(self):
        """Método para listar todos los objetos Celular"""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos")
            return [Celular(*fila) for fila in cursor.fetchall()]

    def eliminar(self, id_producto):
        with self.conectar() as conn:
            conn.execute("DELETE FROM productos WHERE id = ?", (id_producto,))