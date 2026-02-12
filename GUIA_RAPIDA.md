# 🚀 Guía Rápida de Uso

## Inicio Rápido (3 pasos)

### 1️⃣ Instalar (solo la primera vez)
```bash
pip install -r requirements.txt
```

### 2️⃣ Iniciar el servidor
Doble clic en: `iniciar.bat`

O desde la terminal:
```bash
python app.py
```

### 3️⃣ Usar la aplicación
1. Abre tu navegador en: http://localhost:5000
2. Arrastra tu archivo Excel a la zona de carga
3. Haz clic en "Generar PDF" para cada evaluación

## 📋 Requisitos

- Windows 10/11
- Python 3.8 o superior
- Archivo Excel con el formato de evaluaciones

## 🎨 Personalización

### Agregar Logo
1. Coloca tu logo en: `static/logo.png`
2. Formato: PNG (fondo transparente recomendado)
3. Tamaño: 200x50 píxeles

### Modificar Plantilla PDF
Edita el archivo: `templates/reporte.html`

### Cambiar Estilos
Modifica los estilos CSS en: `templates/index.html`

## 📊 Formato del Excel

El sistema espera un Excel con estas columnas:

| Columna | Descripción |
|---------|-------------|
| A | ID |
| B | Hora de inicio |
| C | Hora de finalización |
| D | Correo electrónico |
| E | Nombre |
| F | Cargo |
| G | Área |
| H | Jefe inmediato |
| I | Fecha |
| J | Período |
| K-AX | Calificaciones (1-5) |
| AY | Porcentaje |
| AZ-BC | Preguntas abiertas |

## ⚙️ Configuración Avanzada

### Cambiar Puerto
Edita `app.py`, línea final:
```python
app.run(debug=True, port=5000)  # Cambia 5000 por otro puerto
```

### Tamaño Máximo de Archivo
Edita `app.py`, línea 10:
```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
```

## 🐛 Solución de Problemas

### Error: "Python no está instalado"
- Descarga Python desde: https://www.python.org/downloads/
- Durante la instalación, marca "Add Python to PATH"

### Error: "pip no se reconoce"
- Reinstala Python marcando "Add Python to PATH"
- O usa: `python -m pip install -r requirements.txt`

### Error al generar PDF
- Verifica que WeasyPrint esté instalado correctamente
- En Windows, puede requerir GTK3: https://weasyprint.readthedocs.io/en/stable/install.html

### El logo no aparece
- Verifica que el archivo sea `static/logo.png`
- Formato debe ser PNG, JPG o GIF
- Tamaño recomendado: máximo 50px de altura

### Error al leer Excel
- Verifica que el archivo sea .xlsx o .xls
- Asegúrate de que tenga el formato correcto
- Cierra el archivo Excel antes de cargarlo

## 📞 Soporte

Si encuentras problemas:
1. Revisa esta guía
2. Verifica los mensajes de error en la consola
3. Contacta al equipo de desarrollo

## 🔄 Actualizar

Para actualizar las dependencias:
```bash
pip install -r requirements.txt --upgrade
```

## 🎯 Consejos

- Cierra el archivo Excel antes de cargarlo
- Usa Chrome o Edge para mejor compatibilidad
- Los PDFs se descargan automáticamente
- Puedes generar todos los PDFs a la vez con el botón "Descargar Todos"
