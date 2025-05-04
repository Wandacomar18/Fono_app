from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Ejercicio(Base):
    __tablename__ = 'ejercicios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(Text)
    categoria = Column(String)  # Fonología, Comprensión, etc.

class Evolucion(Base):
    __tablename__ = 'evoluciones'
    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'))
    fecha = Column(String)
    observacion = Column(Text)
