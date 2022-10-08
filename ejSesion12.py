# Importar el módulo sqlite3
import sqlite3
# Importar modulo de error de sqlite3
from sqlite3 import Error
from flask import Flask,request,render_template
import os
from formsEjSesion12 import Producto

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
@app.route('/productos')
def productos(): 
    productos = sql_select_productos()
    return render_template('productos.html', productos = productos)

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if  request.method == "GET": # Si la ruta es accedida a través del método GET entonces
        form = Producto() # Crea un nuevo formulario de tipo producto
        return render_template('nuevo.html', form=form) # Redirecciona vista nuevo.html enviando la variable form
    if  request.method == "POST": # Si la ruta es accedida a través del método POST entonces
        cod = request.form["codigo"] # Asigna variable cod con valor enviado desde formulario  en la vista HTML
        nom = request.form["nombre"] # Asigna variable nom con valor enviado desde formulario en la vista HTML
        cant = request.form["cantidad"] # Asigna variable cant con valor enviado desde formulario en la vista HTML
        sql_insert_producto(cod, nom, cant) # Llamado de la función para insertar el nuevo producto
        return "Consulta correcta"
@app.route('/edit', methods=['GET'])
def editar_producto():
    id = request.args.get('id') # Captura de la variable id enviada a través de la URL
    codigo = request.args.get('codigo') # Captura de la variable código enviada a través de la URL
    nombre = request.args.get('nombre') # Captura de la variable nombre enviada a través de la URL
    cantidad = request.args.get('cantidad') # Captura de la variable cantidad enviada a través de la URL
    sql_edit_producto(id, codigo, nombre, cantidad) # Llamado de la función de edición de la base de datos
    #Consulta Ejemplo -> 127.0.0.1:5000/edit?id=3&codigo=hye&nombre=Uva&cantidad=4
    return "Consulta correcta"
@app.route('/delete', methods=['GET'])
def borrar_producto():
    id = request.args.get('id') # Captura de la variable id enviada a través de la URL
    sql_delete_producto(id) # Llamado a la función de borrado de la base de datos
    #Consulta Ejemplo -> 127.0.0.1/delete?id=3
    return "Consulta correcta"

def sql_connection():
    try:
        con = sqlite3.connect('nrc2103.db')
        return con;
    except Error:
        print(Error)

def sql_insert_producto(codigo, nombre, cantidad):
    strsql="insert into productos (codigo, nombre, cantidad) values ('"+codigo+"','"+nombre+"',"+cantidad+");"
    con=sql_connection()
    cursorObj=con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()
def sql_select_productos():
    strsql = "SELECT * FROM productos;"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    productos = cursorObj.fetchall()
    return productos
def sql_edit_producto(id, codigo, nombre, cantidad):
    strsql = "UPDATE productos SET codigo = '" + codigo + "', nombre = '" + nombre + "', cantidad = " + cantidad + " WHERE id = " + id + ";"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()
def sql_delete_producto(id):
    strsql = "DELETE FROM productos WHERE id = " + id + ";"
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()
