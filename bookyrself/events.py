import flask
import json
from flask import Blueprint, jsonify

import bookyrself

bp = Blueprint("events", __name__, url_prefix="/events")


@bp.route('/<event_id>')
def read_event(event_id):
    return bookyrself.events.child(event_id).get()
