from flask import Blueprint
from app.controllers.parkingspot import update_spot_status, list_spots_by_parking

bp = Blueprint('spots', __name__)

bp.route('/spots/<int:spot_id>', methods=['PATCH'])(update_spot_status)

bp.route('/parkings/<int:parking_id>/spots', methods=['GET'])(list_spots_by_parking)
