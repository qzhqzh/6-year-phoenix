from flask import Flask
from flask import render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object('settings.DevConfig')

mail = Mail(app)

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


if __name__ == '__main__':
    app.run(debug=True)
