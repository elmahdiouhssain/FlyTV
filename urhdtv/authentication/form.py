from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from urhdtv.authentication.models import User, Trial
#from ..models import Client

class RegistrationForm(FlaskForm):

	email = StringField('Email', validators=[DataRequired(), Email(), validators.Length(min=4, max=35)])
	username = StringField('Username', validators=[DataRequired(), validators.Length(min=4, max=25)])
	password = PasswordField('Password', validators=[
										DataRequired(),
										EqualTo('confirm_password'),
										validators.Length(min=8, max=15)
										])
	confirm_password = PasswordField('Confirm Password')

	accept_tos = BooleanField('I accept the Agreements', [validators.DataRequired()])

	submit = SubmitField('Register')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email is already in use.')

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username is already in use.')


class TrialsForm(FlaskForm):

	first_name = StringField('First Name', validators=[DataRequired(), validators.Length(min=4, max=10)])
	last_name = StringField('Last Name', validators=[DataRequired(), validators.Length(min=3, max=10)])
	device_type = StringField('Device Type', validators=[DataRequired(), validators.Length(min=4, max=10)])
	rec_email = StringField('Email', validators=[DataRequired(), Email(), validators.Length(min=4, max=35)])

	trynow = SubmitField('Try Now')


class LoginForm(FlaskForm):
	
	email = StringField('Email', validators=[DataRequired(), Email(), validators.Length(min=4, max=35)])
	password = PasswordField('Password', validators=[DataRequired(), validators.Length(min=8, max=15)])

	submit = SubmitField('Login')