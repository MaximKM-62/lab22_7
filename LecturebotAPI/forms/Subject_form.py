from flask_wtf import FlaskForm
from wtforms import  validators, SubmitField, SelectField, StringField, IntegerField


class Subj_form(FlaskForm):
    pass_num = IntegerField("Subject number:")
    sbname = StringField("Name:")
    student_rating = IntegerField("Rating:")
    gradebook_number = IntegerField("Gradebook number:")
    pass_number = IntegerField("Teacher pass number:")



    submit = SubmitField("Save")