from flask import Blueprint, render_template
import bookyrself

bp = Blueprint("events", __name__, url_prefix="/events")


@bp.route("/")
def get_events():
    events = bookyrself.firebase.database().child('events').get().each()
    return render_template('event/index.html', template_events=events, img_storage=bookyrself.firebase.storage())


@bp.route('/<event_id>')
def read_event(event_id):
    event = bookyrself.firebase.database().child('events').child(event_id).get().val()
    url = bookyrself.firebase.storage().child(f'images/events/{event_id}').get_url(None)
    return render_template('event/event_detail.html', event=event, event_img_url=url)
