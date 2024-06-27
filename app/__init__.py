from flask import Blueprint
from app.routes import *

app = Blueprint('app', __name__, url_prefix='/', template_folder='app/templates', static_folder='app/static')