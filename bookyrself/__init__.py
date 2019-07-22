import flask
import pyrebase

from bookyrself import user, main

app = flask.Flask(__name__)

config = {
    "apiKey": "AIzaSyCTseIzPaKSJnBb_R8nws49Rmv1HzRNejE",
    "authDomain": "bookyrself-staging.firebaseapp.com",
    "databaseURL": "https://bookyrself-staging.firebaseio.com",
    "storageBucket": "bookyrself-staging.appspot.com",
    "serviceAccount": "/Users/benmedcalf/Downloads/bookyrself-staging-firebase-adminsdk-leedp-172ad3a755.json"
}

firebase = pyrebase.initialize_app(config)

app.register_blueprint(user.bp)
app.register_blueprint(main.bp)
app.add_url_rule("/", endpoint="index")

if __name__ == '__main__':
    app.run()