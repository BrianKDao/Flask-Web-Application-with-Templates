from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, EmailField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    vnumber = IntegerField('What is your V number? (without the V)', validators=[DataRequired()])
    first_name = StringField('What is your first name?', validators=[DataRequired()])
    last_name = StringField('What is your last name?', validators=[DataRequired()])
    vcu_email = EmailField('What is your vcu_email?', validators=[DataRequired()])
    coursenumber = SelectField('Enter the Course Number for which you are requesting an override.', choices= (), validators=[DataRequired()])
    submit = SubmitField('Submit')