from urhdtv.administrator import administrator
#from flask_security.decorators import roles_required
from flask import abort, render_template, g, url_for, flash, redirect
from flask_login import current_user, login_required
from urhdtv.authentication.models import User, Trial, Role
#from flask_principal import Principal, Permission, RoleNeed
from flask_dance.contrib.google import google

# Create a permission with a single Need, in this case a RoleNeed.
 #admin_permission = Permission(RoleNeed('administrator'))



@administrator.route('/dashboard')
#@admin_permission.require()

def admin_dashboard():

	if not google.authorized:
		return redirect(url_for("google.login"))
	resp = google.get("/oauth2/v2/userinfo")
	assert resp.ok, resp.text
	return "You are {email} on Google".format(email=resp.json()["email"])



	return render_template('auth/dashboard.html', title="Dashboard")


@administrator.route('/trial')

def trial():

	#with admin_permission.require():

		#trials = Trial.query.all()

	return render_template('auth/trial.html', trials=trials, title="Trials Request")


@administrator.route('/datas')

def datas():

	#with admin_permission.require():

		#clients = User.query.all()

	return render_template('auth/datas.html', clients=clients, title="Clients Registred")