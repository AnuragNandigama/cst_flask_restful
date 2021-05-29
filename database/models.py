from enum import unique
from database.db import db
from flask_bcrypt import check_password_hash, generate_password_hash

#Data Model for Student
class Students(db.Document):
    name = db.StringField(required=True)
    s_id = db.IntField(required=True, unique=True)
    course = db.StringField(required=True)
    program = db.StringField(required=True)
    batch = db.StringField(required=True)
    college = db.StringField(required=True)
    
# Data Model for books
# class Books(db.Document):
#     id = db.IntField(required=True)


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)    
    
    
    
    