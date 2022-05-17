from dataclasses import dataclass
from app import db
from app import login
from flask_login import UserMixin
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post')
    cart = db.relationship('Post', overlaps="posts")
    balance = db.Column(db.Integer)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def delete(self):
        db.session.delete(self)

    def __repr__(self):
        return f'<User {self.username} {self.email}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    price = db.Column(db.Integer)
    is_auction = db.Column(db.SmallInteger)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    filename = db.Column(db.String(256))
    filelink = db.Column(db.String(30))
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    in_cart = db.Column(db.Boolean)

    def __repr__(self):
        return f'<{self.user_id}, {self.timestamp}: {self.body} ({self.price})>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
