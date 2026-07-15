from app.extensions import db

class ParkingSpot(db.Model):
    __tablename__ = 'parking_spot'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=False)
    ocupada = db.Column(db.Boolean, default=False) 
    parking_id = db.Column(db.Integer, db.ForeignKey('parking.id'), nullable=False)

    from flask import request, jsonify
from app.models.parkingspot import ParkingSpot
from app.extensions import db
from app.schemas.parking_schema import spot_schema

def update_spot_status(spot_id):
    spot = ParkingSpot.query.get(spot_id)
    if not spot:
        return jsonify({"erro": "Vaga não encontrada"}), 404
        
    data = request.json
    # O sensor envia se está ocupada ou não
    if 'ocupada' in data:
        spot.ocupada = data['ocupada']
        db.session.commit()
        
    return spot_schema.jsonify(spot)