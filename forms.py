from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Required


COFFEE_CHOICES = ['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕']
WIFI_CHOICES = ['✘' ,'💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
POWER_CHOICES = ['✘' , '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    open_time = StringField('Open', validators=[DataRequired()])
    close_time = StringField('Close', validators=[DataRequired()])
    coffee = SelectField('Coffee', choices=COFFEE_CHOICES, validators=[Required()])
    wifi = SelectField('Wifi', choices=WIFI_CHOICES, validators=[Required()])
    power = SelectField('Power', choices=POWER_CHOICES, validators=[Required()])
    submit = SubmitField('Submit')
