from flask_restful import Resource,Api,abort
from flask import request
from . import bp_api
from .models import Vivienda
from .schemas import ViviendaSchema


api = Api(bp_api)

class ViviendaApiResource(Resource):
    
    def get(self):

        data = Vivienda.get_all()
        vivienda_schema = ViviendaSchema(many=True)
                
        context = {
            'status':True,
            'message':'lista de viviendas',
            'content':vivienda_schema.dump(data)

        }
        
        return context,200

    def post(self):
        data = request.get_json()
        monto_bfh = data.get('monto_bfh')
        monto_ahorro = data.get('monto_ahorro')
        vivienda = Vivienda(monto_bfh, monto_ahorro)
        vivienda.save()

        data_schema = ViviendaSchema()
                
        context = {
            'status':True,
            'message':'vivienda creada',
            'content':data_schema.dump(vivienda)
        }
        return context,201

class ViviendaApiResourceDetail(Resource):
    
    def get_vivienda(self,id):
        viv = Vivienda.get_by_id(id)
        if not viv:
            abort(404, message="vivienda no encontrada")
            
        return viv
    
    def get(self,id):
        data = self.get_vivienda(id)
        data_schema = ViviendaSchema()
        
        context = {
            'status':True,
            'message':'Vivienda encontrada',
            'content': data_schema.dump(data)
        }
        
        return context
    
    def put(self,id):
        data = request.get_json()
        
        
        vivienda = self.get_vivienda(id)
        vivienda.monto_bfh = data.get('monto_bfh')
        vivienda.monto_ahorro = data.get('monto_ahorro')
        vivienda.save()
        
        data_schema = ViviendaSchema()
        
        context = {
            'status':True,
            'message':'Vivienda actualizada',
            'content': data_schema.dump(vivienda)
        }
        
        return context
    
    def delete(self,id):
        vivienda = self.get_vivienda(id)
        vivienda.delete()
        
        context = {
            'status':True,
            'message':'Vivienda eliminada',
        }
        
        return context, 204

api.add_resource(ViviendaApiResource, '/')
api.add_resource(ViviendaApiResourceDetail, '/<int:id>')