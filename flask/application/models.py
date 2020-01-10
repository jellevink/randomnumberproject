from application import db, login_manager
from flask_login import UserMixin
from sqlalchemy.orm import relationship

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    
    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'User Email: ', self.email, '\r\n',
            'User Name: ', self.first_name, ' ', self.last_name
            ])
