from urhdtv.livestream import livestream

from flask import render_template

@livestream.route('/index')
def index():
    return render_template('index/soon.html')