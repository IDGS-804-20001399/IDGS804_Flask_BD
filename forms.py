from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField

from wtforms import validators

class UserForm(Form):
    id = IntegerField("id", [validators.number_range(min=1, max=20, message="Valor no valido")])
    nombre = StringField("nombre", [validators.DataRequired(message="Valor requerido")])
    apaterno = StringField("apaterno", [validators.DataRequired(message="Valor requerido")])
    email = EmailField("email", [validators.DataRequired(message="Valor requerido"),
                                  validators.Email(message="Ingresa un correo valido")])