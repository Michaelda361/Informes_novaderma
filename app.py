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

# Usar /tmp en producción (Render) o carpetas locales en desarrollo
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')
OUTPUT_FOLDER = os.environ.get('OUTPUT_FOLDER', 'output')

# Crear carpetas si no existen (solo en desarrollo)
if not os.path.exists('/tmp'):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
else:
    # En producción usar /tmp
    UPLOAD_FOLDER = '/tmp/uploads'
    OUTPUT_FOLDER = '/tmp/output'
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

def normalizar_texto(texto):
    """Normaliza texto para comparación (minúsculas, sin espacios extras, sin acentos)"""
    if not texto:
        return ''
    import unicodedata
    texto = str(texto).lower().strip()
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    # Eliminar caracteres especiales y espacios múltiples
    texto = ' '.join(texto.split())
    return texto

def encontrar_columna(headers, posibles_nombres, buscar_parcial=True):
    """Busca una columna por varios nombres posibles"""
    headers_norm = [normalizar_texto(h) for h in headers]
    
    for nombre in posibles_nombres:
        nombre_norm = normalizar_texto(nombre)
        
        # Primero buscar coincidencia exacta
        for idx, header in enumerate(headers_norm):
            if nombre_norm == header:
                return idx
        
        # Luego buscar coincidencia parcial si está habilitado
        if buscar_parcial:
            for idx, header in enumerate(headers_norm):
                if nombre_norm in header or header in nombre_norm:
                    return idx
    return None

def extraer_calificaciones_por_categoria(headers, row):
    """Extrae calificaciones agrupadas por categorías"""
    calificaciones = {}
    
    for idx, header in enumerate(headers):
        if idx >= len(row):
            continue
            
        val = row[idx]
        if not isinstance(val, (int, float)) or val <= 0 or val > 5:
            continue
        
        header_norm = normalizar_texto(header)
        
        # Mapear a categorías específicas basadas en palabras clave
        categorias = {
            'organizacion': ['organiza', 'organizacion'],
            'cumple_resultados': ['cumple', 'resultados', 'cumplimiento'],
            'aplica_capacitacion': ['capacitacion', 'entrenamiento', 'formacion', 'aplica'],
            'uso_equipos': ['equipos', 'herramientas', 'uso adecuado', 'elementos'],
            'cumple_politicas': ['politicas', 'normas', 'reglamentos', 'horarios'],
            'conoce_calidad': ['calidad', 'politica de calidad'],
            'propone_mejoras': ['mejoras', 'mejoramiento', 'alternativas', 'ideas'],
            'relaciones': ['relaciones', 'cordialidad', 'interpersonales'],
            'trabajo_equipo': ['equipo', 'colaboracion', 'apoya'],
            'actitud_servicio': ['servicio', 'actitud', 'atencion', 'satisfacer'],
            'comunicacion': ['comunicacion', 'asertiva'],
            'compromiso': ['compromiso', 'objetivos', 'metas'],
            'lealtad': ['lealtad', 'veracidad', 'bienes'],
            'seguridad': ['seguridad', 'salud', 'trabajo', 'actos inseguros'],
            'etica': ['etica', 'responsabilidad social', 'confidencialidad'],
            'orientacion_logro': ['logro', 'meta propuesta'],
            'adaptacion': ['adaptacion', 'cambio'],
        }
        
        # Asignar a la primera categoría que coincida
        for categoria, palabras_clave in categorias.items():
            if categoria not in calificaciones:  # Solo tomar la primera coincidencia
                for palabra in palabras_clave:
                    if palabra in header_norm:
                        calificaciones[categoria] = val
                        break
    
    return calificaciones

def procesar_excel(file_path):
    """Procesa el archivo Excel y extrae los datos de forma flexible"""
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb.active
    
    # Leer encabezados
    headers = [cell.value if cell.value else '' for cell in ws[1]]
    
    # Función auxiliar para verificar si una columna contiene principalmente texto
    def es_columna_texto(col_idx):
        """Verifica si una columna contiene texto en lugar de números"""
        valores_texto = 0
        valores_numero = 0
        for row in ws.iter_rows(min_row=2, max_row=min(10, ws.max_row), values_only=True):
            if col_idx < len(row) and row[col_idx]:
                val = row[col_idx]
                if isinstance(val, str) and len(val) > 10:  # Texto largo
                    valores_texto += 1
                elif isinstance(val, (int, float)) and 1 <= val <= 5:  # Calificación
                    valores_numero += 1
        return valores_texto > valores_numero
    
    # Función mejorada para encontrar columnas de texto
    def encontrar_columna_texto(palabras_clave):
        """Busca columna de texto que contenga las palabras clave"""
        for idx, header in enumerate(headers):
            header_norm = normalizar_texto(header)
            for palabra in palabras_clave:
                palabra_norm = normalizar_texto(palabra)
                if palabra_norm in header_norm and es_columna_texto(idx):
                    return idx
        return None
    
    # Mapeo flexible de columnas - busca por nombres similares
    columnas = {
        'id': encontrar_columna(headers, ['id', 'identificacion', 'numero', 'no'], buscar_parcial=False),
        'nombre': encontrar_columna(headers, ['nombre1', 'nombre', 'empleado', 'trabajador', 'colaborador']),
        'cargo': encontrar_columna(headers, ['cargo', 'puesto', 'posicion']),
        'area': encontrar_columna(headers, ['area', 'departamento', 'seccion']),
        'jefe': encontrar_columna(headers, ['jefe inmediato', 'jefe', 'supervisor', 'evaluador']),
        'fecha': encontrar_columna(headers, ['fecha', 'fecha evaluacion', 'fecha de evaluacion']),
        'periodo': encontrar_columna(headers, ['periodo', 'periodo evaluacion', 'periodo de evaluacion']),
        'porcentaje': encontrar_columna(headers, ['porcentaje', '%', 'puntaje total']),
        # Columnas de texto - usar búsqueda especial
        'aportes': encontrar_columna_texto(['que aportes hizo', 'aportes hizo usted']),
        'mejorar': encontrar_columna_texto(['puede mejorar en el proximo', 'aspectos puede mejorar']),
        'debilidad': encontrar_columna_texto(['debilidad para cumplir', 'area siente debilidad', 'aspecto siente debilidad']),
        'objetivos_alcanzados': encontrar_columna_texto(['objetivos individuales logros', 'logros alcanzo durante', 'objetivos alcanzo durante']),
        'objetivos_futuros': encontrar_columna_texto(['objetivos espera superar', 'espera superar proximo']),
        'porcentaje_cumplimiento': encontrar_columna(headers, ['promedio cumplimiento', 'cumplimiento objetivos', 'porcentaje error']),
        'comentario_jefe': encontrar_columna_texto(['comentarios del jefe inmediato fortalezas', 'comentarios del jefe inmediato']),
        'plan_mejora': encontrar_columna_texto(['plan de mejora propuesto', 'plan mejora propuesto']),
    }
    
    evaluaciones = []
    
    for row_idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        row = list(row) if row else []
        
        # Función auxiliar para obtener valor por nombre de columna
        def get_col(nombre, default=''):
            idx = columnas.get(nombre)
            if idx is None or idx >= len(row):
                return default
            val = row[idx]
            return val if val is not None else default
        
        # Si no hay ID, saltar
        id_val = get_col('id')
        if not id_val:
            continue
        
        # Extraer datos básicos
        evaluacion = {
            'id': id_val,
            'nombre': str(get_col('nombre', '')).upper(),
            'cargo': str(get_col('cargo', '')).upper(),
            'area': str(get_col('area', '')).upper(),
            'jefe': str(get_col('jefe', '')).upper(),
            'fecha': '',
            'periodo': str(get_col('periodo', '')).upper(),
            'porcentaje': get_col('porcentaje', 0),
            'comentario_jefe': str(get_col('comentario_jefe', '')).upper(),
            'plan_mejora': str(get_col('plan_mejora', '')).upper(),
            'aportes': str(get_col('aportes', '')).upper(),
        }
        
        # Formatear fecha
        fecha_val = get_col('fecha')
        if isinstance(fecha_val, datetime):
            evaluacion['fecha'] = fecha_val.strftime('%Y/%m/%d')
        elif fecha_val:
            evaluacion['fecha'] = str(fecha_val)
        
        # Buscar todas las calificaciones numéricas (valores entre 1 y 5)
        calificaciones = []
        for idx, val in enumerate(row):
            if isinstance(val, (int, float)) and 1 <= val <= 5:
                calificaciones.append(val)
        
        # Calcular promedio
        # Primero intentar usar el porcentaje del Excel si existe
        porcentaje_excel = get_col('porcentaje', 0)
        
        if porcentaje_excel and isinstance(porcentaje_excel, (int, float)) and porcentaje_excel > 0:
            # Si el porcentaje está en escala 0-100, convertir a escala 1-5
            if porcentaje_excel > 5:
                promedio = (porcentaje_excel / 100) * 5
            else:
                promedio = porcentaje_excel
        else:
            # Si no hay porcentaje, calcular de las calificaciones
            promedio = sum(calificaciones) / len(calificaciones) if calificaciones else 0
        
        evaluacion['promedio'] = round(promedio, 2)
        evaluacion['rendimiento'] = calcular_rendimiento(promedio)
        
        # Actualizar el porcentaje en la evaluación
        evaluacion['porcentaje'] = round(promedio, 2)
        
        # Extraer calificaciones específicas por categoría
        calificaciones_dict = extraer_calificaciones_por_categoria(headers, row)
        
        evaluacion['calificaciones'] = {
            'organizacion': calificaciones_dict.get('organizacion', 0),
            'cumple_resultados': calificaciones_dict.get('cumple_resultados', 0),
            'aplica_capacitacion': calificaciones_dict.get('aplica_capacitacion', 0),
            'uso_equipos': calificaciones_dict.get('uso_equipos', 0),
            'cumple_politicas': calificaciones_dict.get('cumple_politicas', 0),
            'conoce_calidad': calificaciones_dict.get('conoce_calidad', 0),
            'propone_mejoras': calificaciones_dict.get('propone_mejoras', 0),
            'relaciones': calificaciones_dict.get('relaciones', 0),
            'trabajo_equipo': calificaciones_dict.get('trabajo_equipo', 0),
            'actitud_servicio': calificaciones_dict.get('actitud_servicio', 0),
        }
        
        evaluaciones.append(evaluacion)
    
    return evaluaciones

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test-pdf')
def test_pdf():
    """Endpoint de prueba para verificar que WeasyPrint funciona"""
    try:
        html_simple = """
        <!DOCTYPE html>
        <html>
        <head><meta charset="UTF-8"></head>
        <body>
            <h1>Prueba de PDF</h1>
            <p>Si ves esto, WeasyPrint funciona correctamente.</p>
        </body>
        </html>
        """
        pdf_bytes = HTML(string=html_simple).write_pdf()
        pdf_buffer = BytesIO(pdf_bytes)
        pdf_buffer.seek(0)
        
        return send_file(pdf_buffer, 
                        as_attachment=True,
                        download_name='test.pdf',
                        mimetype='application/pdf')
    except Exception as e:
        import traceback
        return f"Error: {str(e)}<br><br><pre>{traceback.format_exc()}</pre>", 500

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
        # Sanitizar nombre de archivo
        import re
        from werkzeug.utils import secure_filename
        
        # Usar secure_filename pero mantener la extensión
        filename = secure_filename(file.filename)
        if not filename:
            # Si secure_filename elimina todo, usar un nombre genérico con timestamp
            import time
            ext = '.xlsx' if file.filename.endswith('.xlsx') else '.xls'
            filename = f'evaluacion_{int(time.time())}{ext}'
        
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        print(f"Guardando archivo como: {filepath}")
        file.save(filepath)
        
        print(f"Procesando archivo: {filepath}")
        evaluaciones = procesar_excel(filepath)
        print(f"Procesadas {len(evaluaciones)} evaluaciones")
        
        return jsonify({
            'success': True,
            'total': len(evaluaciones),
            'evaluaciones': evaluaciones
        })
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error detallado:\n{error_detail}")
        return jsonify({'error': f'Error al procesar el archivo: {str(e)}'}), 500

@app.route('/generar-pdf/<int:eval_id>', methods=['POST'])
def generar_pdf(eval_id):
    try:
        data = request.json
        evaluacion = data.get('evaluacion')
        
        if not evaluacion:
            return jsonify({'error': 'No se recibieron datos'}), 400
        
        # Obtener logo
        try:
            logo_base64 = get_logo_base64()
        except Exception as e:
            print(f"Advertencia: No se pudo cargar el logo: {e}")
            logo_base64 = ''
        
        # Renderizar HTML
        try:
            html_content = render_template('reporte.html', 
                                          evaluacion=evaluacion,
                                          logo_base64=logo_base64)
        except Exception as e:
            print(f"Error al renderizar template: {e}")
            return jsonify({'error': f'Error al renderizar template: {str(e)}'}), 500
        
        # Generar PDF en memoria
        try:
            pdf_bytes = HTML(string=html_content).write_pdf()
        except Exception as e:
            print(f"Error al generar PDF con WeasyPrint: {e}")
            import traceback
            traceback.print_exc()
            return jsonify({'error': f'Error al generar PDF: {str(e)}'}), 500
        
        # Crear buffer
        pdf_buffer = BytesIO(pdf_bytes)
        pdf_buffer.seek(0)
        
        # Nombre del archivo (sanitizar caracteres especiales)
        nombre_sanitizado = ''.join(c if c.isalnum() or c in (' ', '_') else '_' for c in evaluacion['nombre'])
        pdf_filename = f"evaluacion_{nombre_sanitizado.replace(' ', '_')}_{eval_id}.pdf"
        
        return send_file(pdf_buffer, 
                        as_attachment=True,
                        download_name=pdf_filename,
                        mimetype='application/pdf')
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error general al generar PDF:\n{error_detail}")
        return jsonify({'error': f'Error al generar PDF: {str(e)}'}), 500

if __name__ == '__main__':
    # En desarrollo
    app.run(debug=True, host='0.0.0.0', port=5000)
