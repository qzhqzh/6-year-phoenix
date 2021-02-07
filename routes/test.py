from flask import Blueprint
from flask import render_template
from flask_mail import Message

from ..services import mail
from ..tasks.email import add_together

test = Blueprint('test', __name__)


@test.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@test.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@test.route('/')
def hello(name=None):
    return render_template('hello.html', name=name)

@test.route('/send')
def send():
    msg = Message("Hello",
                  sender="28630707@qq.com",
                  recipients=["28630707@qq.com"])
    mail.send(msg)
    return 'send success!'

@test.route('/add')
def add():
    result = add_together(23, 42)
    #result = add_together.delay(23, 42)
    #result.wait()  # 65
    return 'celery success!'