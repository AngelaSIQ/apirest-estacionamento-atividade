from flask import Blueprint, request
from app.controllers.parking_controller import criar_estacionamento, listar_estacionamentos

bp = Blueprint("parkings", __name__)

bp.route("/", methods=["POST"])(lambda: criar_estacionamento(request.json))
bp.route("/", methods=["GET"])(listar_estacionamentos)
