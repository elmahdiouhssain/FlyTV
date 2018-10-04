from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import ValidationError, DataRequired, Email




class AdminLogin(FlaskForm):
	
	email = StringField('Email', validators=[DataRequired(), Email(), validators.Length(min=4, max=35)])
	pwd_hash = PasswordField('Password', validators=[DataRequired(), validators.Length(min=8, max=15)])
	submit = SubmitField('Login')


class AddnewAdmin(FlaskForm):

	email = StringField('Email', validators=[DataRequired(), Email(), validators.Length(min=4, max=35)])
	full_name = StringField('Full Name', validators=[DataRequired(), validators.Length(min=4, max=25)])
	pwd_hash = PasswordField('Password', validators=[DataRequired(), validators.Length(min=8, max=15)])