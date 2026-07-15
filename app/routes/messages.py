from flask import Blueprint
from app.controllers.parking import create_parking, list_parkings

bp = Blueprint('parkings', __name__, url_prefix='/parkings')

bp.route('/', methods=['POST'])(create_parking)
bp.route('/', methods=['GET'])(list_parkings)
from app.controllers.message_controller import (
    criar_mensagem, 
    listar_mensagens, 
    atualizar_mensagem, 
    deletar_mensagem
)

messages_bp = Blueprint("messages", __name__)


@messages_bp.route("/", methods=["GET"])
def get_messages():
    response, status = listar_mensagens()
    return jsonify(response), status


@messages_bp.route("/", methods=["POST"])
def post_message():
    data = request.get_json()
    response, status = criar_mensagem(data)
    return jsonify(response), status

@messages_bp.route("/<int:id>", methods=["PATCH"])
def patch_message(id):
    r, s = atualizar_mensagem(id, request.get_json())
    return jsonify(r), s

@messages_bp.route("/<int:id>", methods=["DELETE"])
def delete_message(id):
    r, s = deletar_mensagem(id)
    return jsonify(r), s
