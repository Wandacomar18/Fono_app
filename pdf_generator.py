from xhtml2pdf import pisa

def generar_pdf(html_content, output_filename="reporte.pdf"):
    with open(output_filename, "w+b") as f:
        pisa.CreatePDF(html_content, dest=f)
