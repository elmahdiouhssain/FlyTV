# third-party imports

from flask import Flask

from flask_bootstrap import Bootstrap
#from flask_user import login_required, UserManager, UserMixin
from flask_security import Security,  SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
# after existing third-party imports
from flask_login import LoginManager
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Response
from flask_principal import Principal, Permission, RoleNeed


#from urhdtv.authentication.models import Client

# local imports
from config import app_config
from flask_oauth import OAuth

# db variable initialization
db = SQLAlchemy()
# after the db variable initialization
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'this my secretskjsdfsmdkfmsdkfmldkmlskfmlml key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # not using sqlalchemy event system, hence disabling it
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    bootstrap = Bootstrap(app)


    
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.session_protection = 'strong'
    login_manager.login_view = "authentication.login"



    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    # load the extension
    principals = Principal(app)



    return app

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080, debug=True)
        manager.run()


        