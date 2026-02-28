from wtforms import form

from flask import render_template, request, redirect, url_for
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms
from models import Maestros
from flask_migrate import Migrate
from . import maestros
from maestros.routes import maestros, maestros 
from models import db
from models import Alumnos, Maestros


@maestros.route("/maestros", methods=['GET', 'POST'])
@maestros.route("/index")
def index():
    create_form=forms.MaeForm(request.form)
    maestros = Maestros.query.all()
    return render_template("maestros/listadoMae.html", form=create_form,
                           maestros=maestros)

@maestros.route("/creaMae", methods=['GET', 'POST'])
def crear():
	create_form = forms.MaeForm(request.form)
	if request.method=='POST':
		maes=Maestros(nombre=create_form.nombre.data,
			   		 apellidos=create_form.apellidos.data,
					 especialidad=create_form.especialidad.data,
					 email=create_form.email.data)
		db.session.add(maes)
		db.session.commit()
		return redirect(url_for('maestros/index'))
	return render_template("maestros/crearMae.html", form=create_form, maestros=crear)

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"