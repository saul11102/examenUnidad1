from models.persona import Persona
import uuid
from app import db
from datetime import datetime, timedelta
from flask import current_app   
from models.escultura import Escultura

class EsculturaControl:
    escultura = Escultura()
    def listar(self):
        return Escultura.query.all()
        
    def guardarEscultura(self, external_id_persona, data):
        persona = Persona.query.filter_by(external_id = external_id_persona).first()
        if data:
            if persona:
                escultura = Escultura()
                escultura.external_id = uuid.uuid4()
                escultura.nombre = data['nombre']
                escultura.autor = data['autor']
                escultura.estado = True
                escultura.latitud = data['latitud']
                escultura.longitud = data['longitud']
                escultura.persona_id = persona.id

                persona.external_id = uuid.uuid4()

                db.session.merge(persona)

                db.session.add(escultura)
                db.session.commit()
            
                return escultura.id   

            else: 
                return -3

        else:
            return -2
        
    def modificarEscultura(self, external_id_persona, data):
        persona = Persona.query.filter_by(external_id = external_id_persona).first()
        escultura = Escultura.query.filter_by(nombre = data['nombre']).first()
        if data:
            if persona:
                if escultura:
                    escultura.external_id = uuid.uuid4()
                    escultura.autor = data['autor']
                    escultura.estado = True
                    escultura.latitud = data['latitud']
                    escultura.longitud = data['longitud']
                    escultura.persona_id = persona.id

                    persona.external_id = uuid.uuid4()

                    db.session.merge(persona)

                    db.session.merge(escultura)
                    db.session.commit()
                
                    return escultura.id   
                else:
                    return -8
            else:
                return -3

        else:
            return -2
    
    def cambiarEstadoEscultura(self, external_id_persona, data):
        persona = Persona.query.filter_by(external_id = external_id_persona).first()
        escultura = Escultura.query.filter_by(nombre = data['nombre']).first()
        if data:
            if persona:
                if escultura:
                    
                    escultura.persona_id = persona.id

                    if escultura.estado:
                        escultura.estado = False
                    else:
                        escultura.estado = True
                    persona.external_id = uuid.uuid4()

                    db.session.merge(persona)

                    db.session.merge(escultura)
                    db.session.commit()
                
                    return escultura.id   
                else:
                    return -8
            else:
                return -3

        else:
            return -2