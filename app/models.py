from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User (UserMixin,db.Model):
    __tablename__ = 'user'

    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    email = db.Column(db.String(255),unique = True,index = True)

    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)
        

    def __repr__(self):
        return f'User {self.username}'



class Pitch(db.Model):
     __tablename__ = 'pitches'

     id = db.Column(db.Integer,primary_key = True)
     content  = db.Column(db.String(255))
     author = db.Column(db.String(255))
     users = db.relationship('User',backref = 'role',lazy="dynamic")
     
     
     def __repr__(self):
         return f'User {self.name}'

    