from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)


@routes.route("/")
def index():
    return "Hello World!"


@routes.route("/template")
def template():
    return render_template("template.html")
