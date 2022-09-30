from flask import Flask, render_template,flash,redirect,url_for
from forms import FormInicio
app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
@app.route('/')
@app.route('/index')
def index():
    usuario = {'usuario':'...'}
    comentarios = [
        {'autor':{'usuario':'...'}, 'comentario':'...'},
        {'autor':{'usuario':'...'}, 'comentario':'...'}
    ]
    return render_template('base.html', titulo='Inicio', usuario=usuario, comentarios=comentarios)
@app.route('/login',methods=['GET', 'POST'])
def login():
    form = FormInicio()
    if(form.validate_on_submit()):
        flash('Inicio de sesión solicitado por el usuario {}, recordar={}'.format(form.usuario.data,form.recordar.data))
        return redirect(url_for('gracias'))
    return render_template('form.html', form=form)
@app.route('/gracias')
def gracias():
    return render_template('gracias.html')


