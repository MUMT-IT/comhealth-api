from flask import Blueprint

apis = Blueprint('apis', __name__, url_prefix='/api/v1.0')

from . import views