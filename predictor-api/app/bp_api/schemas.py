from utils.db import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import Vivienda

class ViviendaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Vivienda