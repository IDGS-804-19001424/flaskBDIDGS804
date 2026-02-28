from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, EmailField
from wtforms import validators

class UserForm(FlaskForm):
    id = IntegerField("id", [
        validators.NumberRange(min=1, message="valor no valido") 
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El nombre es requerido"),
        validators.Length(min=4, max=20, message="requiere min = 4 mas = 20") 
    ])
    apellidos = StringField("Apellidos", [
        validators.DataRequired(message="El apellido es requerido")
    ])
    email = EmailField("Correo", [
        validators.DataRequired(message="El campo es requerido"), 
        validators.Email(message="Ingrese un correo valido")
    ])
    telefono = StringField("Telefono", [
        validators.DataRequired(message="El campo es requerido")
    ])

class MaeForm(FlaskForm):
    matricula = IntegerField("matricula", [
        validators.NumberRange(min=1, message="valor no valido")
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El nombre es requerido"),
        validators.Length(min=4, max=20, message="requiere min = 4 mas = 20") 
    ])
    apellidos = StringField("Apellidos", [
        validators.DataRequired(message="El apellido es requerido")
    ])
    especialidad = StringField("Especialidad", [
        validators.DataRequired(message="La especialidad es requerida")
    ])
    email = EmailField("Correo", [
        validators.DataRequired(message="El campo es requerido"), 
        validators.Email(message="Ingrese un correo valido")
    ])