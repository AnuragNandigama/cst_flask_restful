from database.db import db

#Data Model for Student
class Students(db.Document):
    name = db.StringField(required=True)
    s_id = db.IntField(required=True, unique=True)
    course = db.StringField(required=True)
    program = db.StringField(required=True)
    batch = db.StringField(required=True)
    college = db.StringField(required=True)
    

