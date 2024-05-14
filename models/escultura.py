from app import db
import uuid
from datetime import datetime

class Escultura(db.Model):
    id        = db.Column(db.Integer, primary_key = True)
    external_id = db.Column(db.String(60), default = str(uuid.uuid4()), nullable = False)
    nombre      = db.Column(db.String(50), nullable = False)
    autor = db.Column(db.String(50), nullable = False)
    estado    = db.Column(db.Boolean, nullable = False, default = True)

    #ubicación
    latitud = db.Column(db.Float, nullable = False)
    longitud = db.Column(db.Float, nullable = False)
    
    #default
    created_at = db.Column(db.DateTime, default = datetime.now)
    updated_at = db.Column(db.DateTime, default = datetime.now, onupdate = datetime.now)

    #foránea
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable = False)

    #relación
    persona = db.relationship('Persona', back_populates='esculturas', lazy=True)

    # methods
    @property
    def serialize(self):
        persona_serialized = self.persona.serialize if self.persona else None
        return {
            'external_id'       : self.external_id,
            'nombre'       : self.nombre,
            'autor' : self.autor,
            'estado'    : self.estado,
            'latitud' : self.latitud,
            'longitud' : self.longitud,
            'persona' : persona_serialized
        }
    
    def copy(self):
        copy_escultura = Escultura(
            nombre       = self.nombre,
            autor = self.autor,
            estado    = self.estado,
            latitud = self.latitud,
            longitud = self.longitud
        )
    
        return copy_escultura