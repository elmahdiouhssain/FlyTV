from flask import Blueprint

livestream = Blueprint('livestream', __name__, template_folder='templates', url_prefix='/index', static_folder='static')


from urhdtv.livestream import views