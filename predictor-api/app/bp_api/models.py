from utils.db import db
from vivienda_predictor import ValorViviendaPredictor

class Vivienda(db.Model):
    __tablename__ = 'vivenda'
    id = db.Column(db.Integer, primary_key=True)
    monto_bfh = db.Column(db.Float, nullable=False)
    monto_ahorro = db.Column(db.Float, nullable=False)
    valor = db.Column(db.Float, nullable=False)

    def __init__(self, monto_bfh, monto_ahorro):
        self.monto_bfh = monto_bfh
        self.monto_ahorro = monto_ahorro
        self.valor = 0.0
    
    @staticmethod
    def get_all():
        return Vivienda.query.all()

    @staticmethod
    def get_by_id(id):
        return Vivienda.query.get(id)
    
    def save(self):
        ml_vivienda = ValorViviendaPredictor()
        self.valor = ml_vivienda.predict(self.monto_bfh, self.monto_ahorro)
        
        if not self.id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()