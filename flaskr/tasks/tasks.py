from ..app import db
from ..models import Song, SongSchema
import os
from celery import Celery
from celery.signals import task_postrun
from config.config import Config

config = Config()

celery_app = Celery('tasks', broker=f'{config.REDIS_BROKER_BASE_URL}/0')

song_schema = SongSchema()

@celery_app.task(name='table.registry')
def register_rating(song_json):
    song = Song.query.get(song_json['id'])
    if song is None:
        song = Song(title=song_json['title'], \
                    minutes=song_json['minutes'], \
                    seconds=song_json['seconds'], \
                    interpreter=song_json['interpreter'], \
                    points=[song_json['point']])
        db.session.add(song)
    else:
        song.points = song.points + [song_json['point']]
    db.session.commit()

@task_postrun.connect
def close_session(*args, **kwargs):
    db.session.remove()