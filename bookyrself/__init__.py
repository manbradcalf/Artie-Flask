import os

import firebase_admin
from firebase_admin import credentials, db, storage
import flask

from bookyrself import user, main

app = flask.Flask(__name__)

creds = credentials.Certificate(os.environ["FIREBASE_CREDS"])
firebase_admin.initialize_app(creds, {
    'databaseURL': 'https://bookyrself-staging.firebaseio.com/'
})


events = db.reference('events')
users = db.reference('users')
images = storage

app.register_blueprint(user.bp)
app.register_blueprint(main.bp)
app.add_url_rule("/", endpoint="index")

if __name__ == '__main__':
    app.run()
