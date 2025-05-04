import pandas as pd
from models import Paciente

def exportar_excel(session, archivo='informe.xlsx'):
    pacientes = session.query(Paciente).all()
    data = [{"Nombre": p.nombre, "Edad": p.edad, "Diagnóstico": p.diagnostico} for p in pacientes]
    df = pd.DataFrame(data)
    df.to_excel(archivo, index=False)
