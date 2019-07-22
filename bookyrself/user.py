import flask
from flask import Blueprint, render_template
import bookyrself

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/")
def get_users():
    template_users = bookyrself.firebase.database().child('users').get().each()
    return render_template('user/index.html', template_users=template_users,
                           img_storage=bookyrself.firebase.storage())


@bp.route('/<user_id>')
def read_user(user_id):
    user = bookyrself.firebase.database().child('users').child(user_id).get().val()
    url = bookyrself.firebase.storage().child(f'images/users/{user_id}').get_url(None)
    return render_template('user/user_detail.html', user=user, user_img_url=url)


@bp.route('/<user_id>/events')
def read_user_events(user_id):
    event_invites = bookyrself.firebase.database().child('users').child(user_id).child('events').get().each()
    events_list = []

    if event_invites is not None:

        for event_id in event_invites:
            event = bookyrself.firebase.database().child('events').child(event_id.key()).get().val()
            events_list.append(event)

    print(events_list)
    return flask.jsonify(events_list)
