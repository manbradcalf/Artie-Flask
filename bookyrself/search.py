from flask import Blueprint, render_template, request
import requests

import bookyrself

bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("/")
def get_search():
    return render_template('search/index.html')


@bp.route('/results')
def execute_search():
    q = request.query_string
    response = requests.get(
        f"https://qtn6r18mt1:vy5800vnq2@dogwood-9512546.us-east-1.bonsaisearch.net:443/users/_search?q={q}")
    results = response.json()['hits']['hits']
    return render_template('search/results.html', results=results, img_storage=bookyrself.firebase.storage())
