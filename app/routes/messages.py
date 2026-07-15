from flask import Blueprint
from app.controllers.parking import create_parking, list_parkings

bp = Blueprint('parkings', __name__, url_prefix='/parkings')

bp.route('/', methods=['POST'])(create_parking)
bp.route('/', methods=['GET'])(list_parkings)
