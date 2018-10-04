from urhdtv.main import main

from flask import render_template


@main.route('/')
def index():
    return render_template('index/index.html')

@main.route('apps')
def apps():
    return render_template('index/apps.html', title='Best Application For Iptv Services')

@main.route('packages')
def packages():
    return render_template('index/packages.html', title='Our Packages')

@main.route('privacy')
def privacy():
    return render_template('index/privacy.html', title='Privacy Policy')

@main.route('terms')
def terms():
    return render_template('index/terms.html', title='Terms Of Use')

@main.route('refund')
def refund():
    return render_template('index/refund.html', title='Refund Policy')

@main.route('404')
def not_found():
    return render_template('index/404.html', title='Not Found !')