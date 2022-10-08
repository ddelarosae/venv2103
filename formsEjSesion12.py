from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Producto(FlaskForm):
    codigo = StringField('Código', validators=[DataRequired(message='No dejar vacío, completar')])
    nombre = StringField('Nombre', validators=[DataRequired()])
    cantidad = IntegerField('Cantidad')
    enviar = SubmitField('Agregar Producto')
