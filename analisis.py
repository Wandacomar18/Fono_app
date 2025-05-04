def generar_pronostico(puntajes):
    if not puntajes:
        return "No hay datos suficientes"
    promedio = sum(puntajes) / len(puntajes)
    if promedio > 80:
        return "Pronóstico excelente: Alta pronta esperada"
    elif promedio > 60:
        return "Pronóstico bueno: Mejora sostenida"
    elif promedio > 40:
        return "Pronóstico reservado: Necesita intervención continua"
    else:
        return "Pronóstico desfavorable: Requiere atención intensiva"
