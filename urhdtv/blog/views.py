from urhdtv.blog import blog

from flask import render_template

@blog.route('/index')
def index():
    return render_template('index/soon2.html')