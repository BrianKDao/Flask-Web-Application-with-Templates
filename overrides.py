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

courses = ["",'cmsc 101', 'cmsc 144', 'cmsc 191', 'cmsc 210', 'cmsc 235', 'cmsc 245', 'cmsc 246', 'cmsc 254', 'cmsc 255', 'cmsc 256', 'cmsc 257', 'cmsc 302', 'cmsc 303', 'cmsc 311', 'cmsc 312', 'cmsc 320', 'cmsc 320', 'cmsc 330', 'cmsc 340', 'cmsc 355', 'cmsc 391', 'cmsc 401', 'cmsc 403', 'cmsc 404', 'cmsc 409', 'cmsc 410', 'cmsc 411', 'cmsc 412', 'cmsc 413', 'cmsc 414', 'cmsc 415', 'cmsc 416', 'cmsc 455', 'cmsc 42069']
class NameForm(FlaskForm):
    vnumber = StringField('What is your V number? (with the V)', validators=[DataRequired()])
    first_name = StringField('What is your first name?', validators=[DataRequired()])
    last_name = StringField('What is your last name?', validators=[DataRequired()])
    vcu_email = EmailField('What is your vcu_email?', validators=[DataRequired()])
    coursenumber = SelectField('Enter the Course Number for which you are requesting an override.', choices=courses, validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.first_name.data
        form.vnumber.data = ''
        form.first_name.data = ''
        form.last_name.data = ''
        form.vcu_email.data = ''
        form.coursenumber.data = ""

    return render_template('index.html', form=form, name=name)

if __name__ == '__main__':
    app.debug=True
    app.run()