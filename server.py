from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Paciente, EvaluacionLenguaje, EvaluacionComunicacion
from export_excel import exportar_excel
from pdf_generator import generar_pdf
from analisis import generar_pronostico
import os

app = Flask(__name__)
DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

@app.route("/")
def index():
    return "App Fonoaudiología OK"

@app.route("/pacientes", methods=["POST"])
def agregar_paciente():
    data = request.json
    paciente = Paciente(nombre=data["nombre"], edad=data["edad"], diagnostico=data["diagnostico"])
    session.add(paciente)
    session.commit()
    return jsonify({"mensaje": "Paciente agregado"})

@app.route("/evaluacion_lenguaje", methods=["POST"])
def agregar_eval_lenguaje():
    data = request.json
    eval = EvaluacionLenguaje(
        paciente_id=data["paciente_id"],
        fecha=data["fecha"],
        tipo_test=data["tipo_test"],
        puntaje=data["puntaje"],
        observaciones=data["observaciones"]
    )
    session.add(eval)
    session.commit()
    return jsonify({"mensaje": "Evaluación de lenguaje guardada"})

@app.route("/pronostico/<int:paciente_id>")
def pronostico(paciente_id):
    evaluaciones = session.query(EvaluacionLenguaje).filter_by(paciente_id=paciente_id).all()
    puntajes = [e.puntaje for e in evaluaciones]
    resultado = generar_pronostico(puntajes)
    return jsonify({"pronostico": resultado})
