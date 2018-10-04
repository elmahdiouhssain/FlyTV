import os
from urhdtv import create_app
from urhdtv.main import main
from urhdtv.authentication import authentication
from urhdtv.authentication.models import User, Clienttype, Trial
from urhdtv.livestream import livestream
from urhdtv.blog import blog
from urhdtv.administrator import administrator
from flask_dance.contrib.google import make_google_blueprint, google

#from urhdtv.authentication.models import User
#from urhdtv.administrator.models import Administrator
from flask import Flask, request, session
from flask_dance.contrib.google import make_google_blueprint, google

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

# Register the blueprints
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(authentication, url_prefix='/authentication')
app.register_blueprint(livestream, url_prefix='/livestream')
app.register_blueprint(blog, url_prefix='/blog')
app.register_blueprint(administrator, url_prefix='/administrator')

blueprint = make_google_blueprint(
    client_id="116453690869-qnsp3olu0fg8dnuqfqr39a3ff6e2jpq4.apps.googleusercontent.com",
    client_secret="E-lPXl1MrBBgGTEv8pgqnqpA",
    scope=[
        "https://www.googleapis.com/auth/plus.me",
        "https://www.googleapis.com/auth/userinfo.email",
    ]
)
app.register_blueprint(blueprint, url_prefix="/login")

print(app.url_map)

#app.run(host='0.0.0.0')