from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates', url_prefix='/index', static_folder='static', static_url_path='file')

from urhdtv.main import views