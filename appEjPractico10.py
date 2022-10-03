from flask import Flask, render_template,redirect,url_for
from formsEjPractico10 import FormInicio
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
@app.route('/',methods=['GET', 'POST'])
def login():
    form = FormInicio()
    if(form.validate_on_submit()):
        return redirect(url_for('ok'))
    return render_template('ejPractico10.html', form=form)
@app.route('/ok')
def ok():
    return render_template('okEjPractico10.html')


