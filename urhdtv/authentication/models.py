from flask_login import UserMixin
from flask_security import RoleMixin, SQLAlchemyUserDatastore
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
from werkzeug.security import generate_password_hash, check_password_hash
from urhdtv import db, login_manager
#from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend


# Define models
roles_users = db.Table('roles_users',
		db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
		db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(80), unique=True)
	description = db.Column(db.String(255))

	def __init__(self, name):
		self.name = name

class User(UserMixin, db.Model):
	"""
	Create an Client table
	"""
	# Ensures table will be named in plural and not in singular
	# as is the name of the model
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(60), index=True, unique=True)
	username = db.Column(db.String(60), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	clienttype_id = db.Column(db.Integer, db.ForeignKey('clienttypes.id'))
	registed_at = db.Column(db.DateTime())
	active = db.Column(db.Boolean())
	roles = db.relationship('Role', secondary=roles_users,
		backref=db.backref('users', lazy='dynamic'))

	@property
	def password(self):
		"""
		Prevent pasword from being accessed
		"""
		raise AttributeError('password is not a readable attribute.')

	@password.setter
	def password(self, password):
		"""
		Set password to a hashed password
		"""
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		"""
		Check if hashed password matches actual password
		"""
		return check_password_hash(self.password_hash, password)

	#def __init__ (self, email, username, password, active, roles):

	@property
	def is_authenticated(self):
		return True
	@property
	def is_anonymous(self):
		return False
	@property
	def roles(self):
		return self.roles
	@property
	def active(self):
		return True

	def get_id(self):
		return str(self.id)


	def __repr__(self):
		return '<User: {}>'.format(self.email)
	

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))



class Trial(db.Model):

	__tablename__ = 'trials'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(60), index=True)
	last_name = db.Column(db.String(60), index=True)
	device_type = db.Column(db.String(60), index=True)
	rec_email = db.Column(db.String(60), index=True, unique=True)
	requested_at = db.Column(db.DateTime())

	def __repr__(self):
		return '<trial: {}>'.format(self.username)

class Clienttype(db.Model):
	"""
	Create a clienttype table
	"""
	__tablename__ = 'clienttypes'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), unique=True)
	description = db.Column(db.String(200))
	Users = db.relationship('User', backref='clienttype',
								lazy='dynamic')

	def __repr__(self):
		return '<clienttype: {}>'.format(self.name)



