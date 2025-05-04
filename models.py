from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey

Base = declarative_base()

class Paciente(Base):
    __tablename__ = 'pacientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)
    diagnostico = Column(Text)

class EvaluacionLenguaje(Base):
    __tablename__ = 'evaluaciones_lenguaje'
    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'))
    fecha = Column(String)
    tipo_test = Column(String)
    puntaje = Column(Integer)
    observaciones = Column(Text)

class EvaluacionComunicacion(Base):
    __tablename__ = 'evaluaciones_comunicacion'
    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'))
    fecha = Column(String)
    area = Column(String)
    resultado = Column(String)
    observaciones = Column(Text)
