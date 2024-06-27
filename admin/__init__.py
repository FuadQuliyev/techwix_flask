from flask import Blueprint
from admin.routes import *

admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='admin/templates', static_folder='admin/static')