import flask
from flask import Blueprint, jsonify, render_template

import bookyrself

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route('/<user_id>')
def read_user(user_id):
    user = bookyrself.users.child(user_id).get()
    return render_template('user/index.html', user=user, user_id=user_id)


@bp.route('/<user_id>/events')
def read_user_events(user_id):
    event_invites = bookyrself.users.child(user_id).child('events').get()
    events_list = []
    for event_id in event_invites:
        event = bookyrself.events.child(event_id).get()
        events_list.append(event)

    return flask.jsonify(events_list)
