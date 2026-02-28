from flask import render_template, request, redirect, url_for, flash
import forms
from models import db, Curso, Alumnos, Maestros
from . import cursos

@cursos.route("/", methods=['GET'])
@cursos.route("/cursos", methods=['GET'])
def index():
    lista_cursos = Curso.query.all()
    return render_template("cursos/index.html", cursos=lista_cursos)

@cursos.route("/crearCurso", methods=['GET', 'POST'])
def crear():
    maestros_disponibles = Maestros.query.all()
    
    if request.method == 'POST':
        nuevo_curso = Curso(
            nombre=request.form.get('nombre'),
            descripcion=request.form.get('descripcion'),
            maestro_id=request.form.get('maestro_id')
        )
        db.session.add(nuevo_curso)
        db.session.commit()
        return redirect(url_for('cursos.index'))
        
    return render_template("cursos/crear.html", maestros=maestros_disponibles)


@cursos.route("/inscribirCurso", methods=['GET', 'POST'])
def inscribir():
    """Agrega un alumno a un curso existente."""
    if request.method == 'POST':
        curso_id = request.form.get('curso_id')
        alumno_id = request.form.get('alumno_id')
        
        curso = db.session.query(Curso).filter(Curso.id == curso_id).first()
        alumno = db.session.query(Alumnos).filter(Alumnos.id == alumno_id).first()
        
        if curso and alumno:
            if alumno not in curso.alumnos:
                curso.alumnos.append(alumno)
                db.session.commit()
            
        return redirect(url_for('cursos.detalles', id=curso.id))
    
    cursos_lista = Curso.query.all()
    alumnos_lista = Alumnos.query.all()
    return render_template("cursos/inscribir.html", cursos=cursos_lista, alumnos=alumnos_lista)

@cursos.route("/detallesCurso", methods=['GET'])
def detalles():
    curso_id = request.args.get('id')
    curso = db.session.query(Curso).filter(Curso.id == curso_id).first()
    
    if not curso:
        return redirect(url_for('cursos.index'))

    todos_los_alumnos = Alumnos.query.all()
    
    alumnos_disponibles = [alumno for alumno in todos_los_alumnos if alumno not in curso.alumnos]
    
    return render_template("cursos/detalles.html", curso=curso, alumnos_disponibles=alumnos_disponibles)

@cursos.route("/perfil_alumno", methods=['GET'])
def perfil_alumno():
    """Muestra el perfil de un alumno y los cursos que está tomando."""
    alumno_id = request.args.get('id')
    alumno = db.session.query(Alumnos).filter(Alumnos.id == alumno_id).first()
    
    
    return render_template("cursos/perfil_alumno.html", alumno=alumno)


@cursos.route("/agregar_alumno_rapido/<int:curso_id>", methods=['POST'])
def agregar_alumno_rapido(curso_id):
    alumno_id = request.form.get('alumno_id')
    
    curso = db.session.query(Curso).filter(Curso.id == curso_id).first()
    alumno = db.session.query(Alumnos).filter(Alumnos.id == alumno_id).first()
    
    if curso and alumno and alumno not in curso.alumnos:
        curso.alumnos.append(alumno) 
        db.session.commit()
        
    return redirect(url_for('cursos.detalles', id=curso.id))