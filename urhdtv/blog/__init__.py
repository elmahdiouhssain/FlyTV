from flask import Blueprint

blog = Blueprint('blog', __name__, template_folder='templates', url_prefix='/index', static_folder='static')


from urhdtv.blog import views