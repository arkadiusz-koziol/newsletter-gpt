from src import db
from flask_login import UserMixin
from src import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150))
    topics = db.Column(db.String(250))  # e.g., "technology,health,science"

    def __repr__(self):
        return f'<User {self.email}>'

