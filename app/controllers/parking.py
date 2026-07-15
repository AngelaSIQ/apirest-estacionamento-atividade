from app.extensions import db

class Parking(db.Model):
    __tablename__ = 'parking'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    # Relacionamento: um estacionamento tem várias vagas
    spots = db.relationship('ParkingSpot', backref='parking', lazy=True)
