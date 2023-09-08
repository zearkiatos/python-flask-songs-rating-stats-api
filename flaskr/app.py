from flaskr import create_app
from flask_restful import Api, Resource
from .models.song import db, Song, SongSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

song_schema = SongSchema()

class ViewRatingTable(Resource):
    def get(self):
        return [song_schema.dump(song) for song in Song.query.all()]
    

api = Api(app)
api.add_resource(ViewRatingTable, '/ratingTable')