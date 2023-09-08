from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..dataContext import db
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import Float, String

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    minutes = db.Column(db.Integer)
    seconds = db.Column(db.Integer)
    interpreter = db.Column(db.String(128))
    points = db.Column(ARRAY(Float))

    def __representation__(self):
        return "{}-{}-{}-{}".format(self.title, self.minutes, self.minutes, self.seconds, self.interpreter)
    
class SongSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Song
        load_instance = True