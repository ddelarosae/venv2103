from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class FormInicio(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío, completar')])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacío, completar')])
    recordar = BooleanField('Recordar Usuario')
    enviar = SubmitField('Iniciar Sesión')
