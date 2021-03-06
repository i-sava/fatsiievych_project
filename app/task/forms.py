from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, SelectField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired, Optional
from .models import *


# метод для витягування списку категорій з БД
def getСategoryList():
    categ_list = []
    categories = Category.query.all()
    for categ in categories:
        categ_list.append((categ.id, categ.name))
    return categ_list


def getEmployeeList():
    empl_list = []
    employes = Employee.query.all()
    for emp in employes:
        empl_list.append((emp.id, emp.name))
    return empl_list


class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])

    description = TextAreaField('Description', validators=[DataRequired()])

    # created = DateTimeField('Created', format='%d-%m-%Y %H:%M:%S', validators=[])
    # ValidationError(message="Введіть дату у форматі y-m-d")
    created = DateField('Created', format='%Y-%m-%d', validators=[Optional()])

    priority = SelectField('Priority', choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')])

    category = SelectField('Category', coerce=int)

    employee = SelectMultipleField('Employee', coerce=int)

    is_done = BooleanField('Is done')

    submit = SubmitField('Submit')

    @classmethod
    def new(cls):
        form = cls()

        form.category.choices = getСategoryList()
        form.employee.choices = getEmployeeList()
        return form


class CategoryForm(FlaskForm):
    name = StringField('Category name', validators=[DataRequired()])

    submit = SubmitField('Submit')


class EmployeeForm(FlaskForm):
    name = StringField('Employee name', validators=[DataRequired()])

    submit = SubmitField('Submit')