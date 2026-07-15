from flask import Blueprint, request
from app.controllers.parking_spot_controller import criar_vaga, listar_vagas, atualizar_status_vaga

bp = Blueprint("spots", __name__)

bp.route("/", methods=["POST"])(lambda: criar_vaga(request.json))
bp.route("/", methods=["GET"])(listar_vagas)
bp.route("/<int:spot_id>", methods=["PATCH"])(lambda spot_id: atualizar_status_vaga(spot_id, request.json))
