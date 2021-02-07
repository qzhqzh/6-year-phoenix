from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'bd_user'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(255))
    image = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('db_roles.rid'))


class Role(db.Model):
    __tablename__ = 'db_roles'
    rid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role")
