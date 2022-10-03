from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class FormInicio(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío, completar')])
    correo = EmailField('Correo Electrónico')
    mensaje = TextAreaField('Mensaje')
    enviar = SubmitField('Enviar')
