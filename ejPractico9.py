from flask import Flask, render_template, request, flash, jsonify,json
import utils
import yagmail
import os
from mensaje import mensaje
app = Flask(__name__)
app.secret_key = os.urandom(24)
@app.route('/')
def index():
    return render_template('sesion.html')
@app.route('/error')
def error():
    return render_template('error.html')
@app.route('/mensajes')
def mensajes():
    return jsonify(mensaje)
@app.route('/productos/<string:nom_articulo>')
@app.route('/login',methods=('GET','POST'))
def login():
        try:
            if request.method == 'POST':
                return json.dumps(mensaje)
        except:
            return render_template('error.html') 
@app.route('/sesion',methods=('GET','POST'))
def sesion():
    try:
        if request.method == 'POST':
            username = request.form['usuario']
            password = request.form['pass']
            email = request.form['correo']
            if not utils.isUsernameValid(username):
                error="El usuario debe ser alfanumerico"
                flash(error)
                return render_template('sesion.html')
            if not utils.isPasswordValid(password):
                error="La contraseña debe tener al menos 8 caracteres"
                flash(error)
                return render_template('sesion.html')
            if not utils.isEmailValid(email):
                error="El email debe ser alfanumerico"
                flash(error)
                return render_template('sesion.html')
            yag=yagmail.SMTP('danieldelarosa.ruta1@utp.edu.co','Qn$w+?3x.ACg')
            yag.send(to=email, subject='Cuenta creada', contents='Se ha creado su usuario')
            flash('Verifique su correo electronico')
            return render_template('ejPractico9_login.html')
        return render_template('sesion.html')
    except:
        return render_template('sesion.html')        