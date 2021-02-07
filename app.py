from celery import Celery
from flask import Flask
from flask import render_template
from flask_mail import Mail, Message
from tasks.email import add_together


app = Flask(__name__)
app.config.from_object('settings.DevConfig')
mail = Mail(app)

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)


@app.route('/')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/send')
def send():
    msg = Message("Hello",
                  sender="28630707@qq.com",
                  recipients=["28630707@qq.com"])
    mail.send(msg)
    return 'send success!'

@app.route('/add')
def add():
    result = add_together.delay(23, 42)
    result.wait()  # 65
    return 'celery success!'

if __name__ == '__main__':
    app.run(debug=True)
