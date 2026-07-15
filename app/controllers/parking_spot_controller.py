from app.extensions import db
from app.models.parking_spot import ParkingSpot
from app.models.parking import Parking
from app.schemas.parking_spot_schema import ParkingSpotSchema
from app.utils.response import success_response


spot_schema = ParkingSpotSchema()
spots_schema = ParkingSpotSchema(many=True)


def criar_vaga(data):
    dados_validados = spot_schema.load(data)

    Parking.query.get_or_404(dados_validados["parking_id"])

    nova_vaga = ParkingSpot(**dados_validados)

    db.session.add(nova_vaga)
    db.session.commit()

    return success_response(spot_schema.dump(nova_vaga), 201)


def listar_vagas():
    vagas = ParkingSpot.query.all()
    return success_response(spots_schema.dump(vagas))


def atualizar_status_vaga(spot_id, data):
    vaga = ParkingSpot.query.get_or_404(spot_id)

    if "ocupada" in data:
        vaga.ocupada = data["ocupada"]
        db.session.commit()

    return success_response(spot_schema.dump(vaga))
