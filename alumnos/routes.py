from flask import render_template, request, redirect, url_for
import forms
from models import db, Alumnos
from . import alumnos

@alumnos.route("/", methods=['GET','POST'])
@alumnos.route("/alumnos")
def index():
    create_form = forms.UserForm(request.form)
    alumnos_list = Alumnos.query.all()
    return render_template("alumnos/index.html", form=create_form, alumno=alumnos_list)

@alumnos.route("/alum", methods=['GET', 'POST'])
def alumnos_route():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre=create_form.nombre.data,
                       apellidos=create_form.apellidos.data,
                       email=create_form.email.data,
                       telefono=create_form.telefono.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.index'))
    
    alumnos_list = Alumnos.query.all()
    return render_template("alumnos/Alumnos.html", form=create_form, alumno=alumnos_list)

@alumnos.route("/detalles", methods=['GET', 'POST'])
def detalles():
    id = ""
    nombre = ""
    apellidos = ""
    email = ""
    telefono = ""
    
    if request.method == 'GET':
        id = request.args.get('id')
        if id: 
            alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
            if alum1:
                nombre = alum1.nombre
                apellidos = alum1.apellidos
                email = alum1.email
                telefono = alum1.telefono
                
    return render_template('alumnos/detalles.html', id=id, nombre=nombre, apellidos=apellidos, email=email, telefono=telefono)

@alumnos.route("/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        if alum1:
            create_form.id.data = id
            create_form.nombre.data = alum1.nombre
            create_form.apellidos.data = alum1.apellidos
            create_form.email.data = alum1.email
            create_form.telefono.data = alum1.telefono

    if request.method == 'POST':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        if alum1:
            alum1.nombre = create_form.nombre.data
            alum1.apellidos = create_form.apellidos.data
            alum1.email = create_form.email.data
            alum1.telefono = create_form.telefono.data
            db.session.commit()
            return redirect(url_for('alumnos.index'))
            
    alumnos_list = Alumnos.query.all()
    return render_template("alumnos/modificar.html", form=create_form, alumno=alumnos_list)

@alumnos.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        if alum1:
            create_form.id.data = id
            create_form.nombre.data = alum1.nombre
            create_form.apellidos.data = alum1.apellidos
            create_form.email.data = alum1.email
            create_form.telefono.data = alum1.telefono

    if request.method == 'POST':
        id = create_form.id.data
        alum = Alumnos.query.get(id)
        if alum:
            db.session.delete(alum)
            db.session.commit()
        return redirect(url_for('alumnos.index'))
        
    alumnos_list = Alumnos.query.all()
    return render_template("alumnos/eliminar.html", form=create_form, alumno=alumnos_list)