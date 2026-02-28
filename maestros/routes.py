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
		return redirect(url_for('maestros.index'))
	return render_template("maestros/crearMae.html", form=create_form)

@maestros.route("/modificarMae", methods=['GET', 'POST'])
def modificar():
	create_form = forms.MaeForm(request.form)
	if request.method=='GET':
		matricula = request.args.get('matricula')
		mae1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		create_form.matricula.data=request.args.get('matricula')
		create_form.nombre.data=mae1.nombre
		create_form.apellidos.data=mae1.apellidos
		create_form.especialidad.data=mae1.especialidad
		create_form.email.data=mae1.email

	if request.method=='POST':
		matricula = request.args.get('matricula')
		mae1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		mae1.matricula=matricula
		mae1.nombre=nombre=create_form.nombre.data
		mae1.apellidos=apellidos=create_form.apellidos.data
		mae1.especialiadad=especialidad=create_form.especialidad.data
		mae1.email=email=create_form.email.data
		db.session.add(mae1)
		db.session.commit()
		return redirect(url_for('maestros.index'))
	return render_template("maestros/modificarMae.html", form=create_form)

@maestros.route("/detallesMae", methods=['GET', 'POST'])
def detalles():
    create_form = forms.UserForm(request.form)
    matricula = ""
    nombre = ""
    apellidos = ""
    especialidad = ""
    email = ""
    
    if request.method == 'GET':
        matricula = request.args.get('matricula')
        if matricula: 
            mae1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
            if mae1:
                nombre = mae1.nombre
                apellidos = mae1.apellidos
                especialidad = mae1.especialidad
                email = mae1.email
                
    return render_template('maestros/detallesMae.html', matricula=matricula, nombre=nombre, apellidos=apellidos, especialidad=especialidad, email=email)

@maestros.route("/eliminarMae", methods=['GET', 'POST'])
def eliminar():
	create_form = forms.MaeForm(request.form)
	if request.method=='GET':
		matricula = request.args.get('matricula')
		mae1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		create_form.matricula.data=request.args.get('matricula')
		create_form.nombre.data=mae1.nombre
		create_form.apellidos.data=mae1.apellidos
		create_form.especialidad.data=mae1.especialidad
		create_form.email.data=mae1.email

	if request.method=='POST':
		matricula = create_form.matricula.data
		mae = Maestros.query.get(matricula)
		db.session.delete(mae)
		db.session.commit()
		return redirect(url_for('maestros.index'))
	return render_template("maestros/eliminarMae.html", form=create_form)


@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"