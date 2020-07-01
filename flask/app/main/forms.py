from flask_wtf import FlaskForm
from wtforms.fields import SelectField, StringField, SubmitField
from wtforms.validators import Required


class LoginForm(FlaskForm):
    """Accepts a nickname and a room."""
    name = StringField('Name', validators=[Required()])
    room = StringField('Room', validators=[Required()])
    option = SelectField('Destination', choices=[('trial', 'Trial'), ('chat', 'General chat')])
    submit = SubmitField('Enter Chatroom')
