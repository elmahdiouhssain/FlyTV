from flask import Blueprint

authentication = Blueprint('authentication', __name__, template_folder='templates', url_prefix='/users', static_folder='static')


from urhdtv.authentication import views