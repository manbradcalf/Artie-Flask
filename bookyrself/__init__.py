import os
import flask
import pyrebase

from bookyrself import user, main, event, about, search

app = flask.Flask(__name__)

config = {
    "apiKey": os.environ['FIREBASE_API_KEY'],
    "authDomain": "bookyrself-staging.firebaseapp.com",
    "databaseURL": "https://bookyrself-staging.firebaseio.com",
    "storageBucket": "bookyrself-staging.appspot.com",
    "serviceAccount": "google-credentials.json"
}

firebase = pyrebase.initialize_app(config)

app.register_blueprint(user.bp)
app.register_blueprint(main.bp)
app.register_blueprint(event.bp)
app.register_blueprint(about.bp)
app.register_blueprint(search.bp)
app.add_url_rule("/", endpoint="index")

if __name__ == '__main__':
    app.run()
