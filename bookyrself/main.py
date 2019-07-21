from flask import Blueprint, render_template

bp = Blueprint("main", __name__, url_prefix="")


@bp.route('/')
def index():
    return render_template("home/base.html", header_text="this is a header")
