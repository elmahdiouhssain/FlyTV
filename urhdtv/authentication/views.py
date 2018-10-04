from flask import flash, redirect, render_template, url_for, abort, request
from werkzeug.urls import url_parse
from flask_login import login_required, login_user, logout_user, current_user
from urhdtv.authentication import authentication
from . import authentication
from form import LoginForm, RegistrationForm, TrialsForm
from .. import db
from urhdtv.authentication.models import User, Trial

######################################################################################

@authentication.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
							username=form.username.data,
							password=form.password.data)

		# add employee to the database
		db.session.add(user)
		db.session.commit()
		flash('You have successfully registered! You may now login.')

		# redirect to the login page
		return redirect(url_for('authentication.login'))

	# load registration template
	return render_template('users/register.html', form=form, title='Register')

@authentication.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an Client in through the login form
    """
    if current_user.is_authenticated:
		return redirect(url_for('authentication.area'))
    form = LoginForm()
    if form.validate_on_submit():

        # check whether Client exists in the database and whether
        # the password entered matches the password in the database
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            # log Client in
            login_user(user)

            # redirect to the dashboard page after login
            return redirect(url_for('authentication.area'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('users/index.html', form=form, title='Login')
	# ...
######################################################################################

@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@authentication.route('/area', methods=['GET', 'POST'])
@login_required
def area():

	###----Trial Form ----###

	form = TrialsForm()
	if form.validate_on_submit():
		trial = Trial(first_name=form.first_name.data,
					  last_name=form.last_name.data,
					  device_type=form.device_type.data,
					  rec_email =form.rec_email.data)

		# Add to Database Trials###$ $
		db.session.add(trial)
		db.session.commit()
		flash('GreaT *_* : Your Trial Request will be Sent To your Email before 24H .')

		# resirect to the dashboard
		return redirect(url_for('authentication.area'))

	# load trial template
	return render_template('users/pricing.html', form=form, title='Clients Area')

######################################################################################




