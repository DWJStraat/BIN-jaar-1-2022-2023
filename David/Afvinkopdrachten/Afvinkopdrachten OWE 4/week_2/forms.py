from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class DNAForm(FlaskForm):
    dna = StringField('DNA', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()], render_kw={"type": "password"})
    submit = SubmitField('Submit')

class StudentForm(FlaskForm):
    student_id = StringField('Student nummer', validators=[DataRequired()])
    submit = SubmitField('Submit')