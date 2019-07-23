import os

import flask
import pyrebase

from bookyrself import user, main, event

app = flask.Flask(__name__)

config = {
    "apiKey": os.environ['FIREBASE_API_KEY'],
    "authDomain": "bookyrself-staging.firebaseapp.com",
    "databaseURL": "https://bookyrself-staging.firebaseio.com",
    "storageBucket": "bookyrself-staging.appspot.com",
    "serviceAccount": os.environ['GOOGLE_CREDENTIALS']
}

firebase = pyrebase.initialize_app(config)

app.register_blueprint(user.bp)
app.register_blueprint(main.bp)
app.register_blueprint(event.bp)
app.add_url_rule("/", endpoint="index")

if __name__ == '__main__':
    app.run()
