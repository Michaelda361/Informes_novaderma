from flask import Flask, render_template, request, send_file, jsonify
import openpyxl
from datetime import datetime
import os
import base64
from io import BytesIO
from weasyprint import HTML, CSS
import tempfile

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def get_logo_base64():
    """Retorna el logo en base64 si existe"""
    logo_path = 'static/logo.png'
    if os.path.exists(logo_path):
        with open(logo_path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    return ''

def calcular_rendimiento(promedio):
    """Calcula la clasificación del rendimiento"""
    if promedio >= 4.5:
        return 'Sobresaliente'
    elif promedio >= 3.5:
        return 'Satisfactorio'
    elif promedio >= 2.5:
        return 'Aceptable'
    elif promedio >= 1.5:
        return 'No Satisfactorio'
    else:
        return 'Deficiente'

def procesar_excel(file_path):
    """Procesa el archivo Excel y extrae los datos"""
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb.active
    
    evaluaciones = []
    headers = [cell.value for cell in ws[1]]
    
    for row_idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        if not row[0]:  # Si no hay ID, saltar
            continue
            
        # Extraer datos básicos
        evaluacion = {
            'id': row[0],
            'nombre': row[4] or '',
            'cargo': row[5] or '',
            'area': row[6] or '',
            'jefe': row[7] or '',
            'fecha': '',
            'periodo': row[9] or '',
            'porcentaje': row[46] or 0,
            'comentario_jefe': row[51] or '',
            'plan_mejora': row[52] or '',
            'aportes': row[47] or '',
        }
        
        # Formatear fecha de evaluación
        if isinstance(row[8], datetime):
            evaluacion['fecha'] = row[8].strftime('%Y/%m/%d')
        elif row[8]:
            evaluacion['fecha'] = str(row[8])
        else:
            evaluacion['fecha'] = ''
        
        # Calcular promedio de las calificaciones (columnas 10-46)
        calificaciones = [row[i] for i in range(10, 46) if isinstance(row[i], (int, float))]
        promedio = sum(calificaciones) / len(calificaciones) if calificaciones else 0
        
        evaluacion['promedio'] = round(promedio, 2)
        evaluacion['rendimiento'] = calcular_rendimiento(promedio)
        
        # Extraer calificaciones específicas para el reporte
        evaluacion['calificaciones'] = {
            'organizacion': row[11] or 0,
            'cumple_resultados': row[12] or 0,
            'aplica_capacitacion': row[19] or 0,
            'uso_equipos': row[10] or 0,
            'cumple_politicas': row[25] or 0,
            'conoce_calidad': row[28] or 0,
            'propone_mejoras': row[29] or 0,
            'relaciones': row[43] or 0,
            'trabajo_equipo': row[44] or 0,
            'actitud_servicio': row[41] or 0,
        }
        
        evaluaciones.append(evaluacion)
    
    return evaluaciones

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No se envió ningún archivo'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400
    
    if not file.filename.endswith(('.xlsx', '.xls')):
        return jsonify({'error': 'El archivo debe ser Excel (.xlsx o .xls)'}), 400
    
    try:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        evaluaciones = procesar_excel(filepath)
        
        return jsonify({
            'success': True,
            'total': len(evaluaciones),
            'evaluaciones': evaluaciones
        })
    except Exception as e:
        return jsonify({'error': f'Error al procesar el archivo: {str(e)}'}), 500

@app.route('/generar-pdf/<int:eval_id>', methods=['POST'])
def generar_pdf(eval_id):
    try:
        data = request.json
        evaluacion = data.get('evaluacion')
        
        if not evaluacion:
            return jsonify({'error': 'No se recibieron datos'}), 400
        
        logo_base64 = get_logo_base64()
        html_content = render_template('reporte.html', 
                                      evaluacion=evaluacion,
                                      logo_base64=logo_base64)
        
        pdf_filename = f"evaluacion_{evaluacion['nombre'].replace(' ', '_')}_{eval_id}.pdf"
        pdf_path = os.path.join(OUTPUT_FOLDER, pdf_filename)
        
        HTML(string=html_content).write_pdf(pdf_path)
        
        return send_file(pdf_path, 
                        as_attachment=True,
                        download_name=pdf_filename,
                        mimetype='application/pdf')
    except Exception as e:
        return jsonify({'error': f'Error al generar PDF: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
