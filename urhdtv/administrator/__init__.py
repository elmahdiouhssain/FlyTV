from flask import Blueprint

administrator = Blueprint('administrator', __name__, template_folder='templates', url_prefix='/auth', static_folder='static')


from urhdtv.administrator import views