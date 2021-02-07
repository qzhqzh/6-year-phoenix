from .celery import make_celery
from .email import mail

def init_app(app):
    mail.init_app(app)
