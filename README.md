# 📊 Generador de Reportes de Evaluación - Novaderma

Sistema web para procesar archivos Excel de evaluaciones de desempeño y generar reportes profesionales en PDF.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Características

- ✅ Interfaz web moderna y responsive
- ✅ Carga de archivos Excel (.xlsx, .xls) por drag & drop
- ✅ Procesamiento automático de evaluaciones
- ✅ Generación de PDFs individuales o masivos
- ✅ Clasificación automática de rendimiento
- ✅ Logo personalizable
- ✅ 100% local y privado (no requiere internet para funcionar)

## 📸 Capturas de Pantalla

### Interfaz Principal
Interfaz moderna con drag & drop para cargar archivos Excel.

### Tabla de Evaluaciones
Vista previa de todas las evaluaciones con clasificación de rendimiento.

### Reporte PDF Generado
Documento profesional con formato corporativo.

## 🚀 Inicio Rápido

### Requisitos Previos

- Python 3.8 o superior
- pip (incluido con Python)

### Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/novaderma-reportes.git
   cd novaderma-reportes
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Agregar logo (opcional)**
   - Colocar el logo en: `static/logo.png`
   - Formato recomendado: PNG, 200x50 píxeles

4. **Iniciar la aplicación**
   
   **Windows:**
   ```bash
   iniciar.bat
   ```
   
   **Linux/Mac:**
   ```bash
   python app.py
   ```

5. **Abrir en el navegador**
   ```
   http://localhost:5000
   ```

## 📋 Uso

1. **Cargar archivo Excel**
   - Arrastra el archivo a la zona de carga
   - O haz clic en "Seleccionar Archivo"

2. **Revisar evaluaciones**
   - La tabla muestra todas las evaluaciones encontradas
   - Verifica nombres, cargos y promedios

3. **Generar PDFs**
   - Clic en "Generar PDF" para una evaluación específica
   - O "Descargar Todos los PDF" para generar todos

## 📊 Formato del Excel

El archivo Excel debe contener las siguientes columnas:

| Columna | Descripción |
|---------|-------------|
| A | ID |
| B-C | Hora de inicio/fin |
| D | Correo electrónico |
| E | Nombre del colaborador |
| F | Cargo |
| G | Área |
| H | Jefe inmediato |
| I | Fecha de evaluación |
| J | Período evaluado |
| K-AX | Calificaciones (1-5) |
| AY | Porcentaje de cumplimiento |
| AZ-BC | Comentarios y plan de mejora |

## 🎨 Clasificación de Rendimiento

| Clasificación | Promedio | Color |
|---------------|----------|-------|
| Sobresaliente | ≥ 4.5 | 🟢 Verde |
| Satisfactorio | 3.5 - 4.49 | 🔵 Azul |
| Aceptable | 2.5 - 3.49 | 🟠 Naranja |
| No Satisfactorio | 1.5 - 2.49 | 🔴 Rojo |
| Deficiente | < 1.5 | ⚫ Negro |

## 🛠️ Tecnologías

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Generación PDF:** WeasyPrint
- **Procesamiento Excel:** openpyxl
- **Imágenes:** Pillow

## 📁 Estructura del Proyecto

```
novaderma-reportes/
├── app.py                          # Aplicación Flask principal
├── requirements.txt                # Dependencias Python
├── iniciar.bat                     # Script de inicio (Windows)
├── README.md                       # Este archivo
├── templates/
│   ├── index.html                  # Interfaz web principal
│   └── reporte.html                # Plantilla para PDFs
├── static/
│   └── logo.png                    # Logo de la empresa
├── uploads/                        # Archivos Excel cargados (temporal)
└── output/                         # PDFs generados (temporal)
```

## ⚙️ Configuración

### Cambiar Puerto

Edita `app.py`, última línea:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Cambia 5000
```

### Tamaño Máximo de Archivo

Edita `app.py`, línea 10:
```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
```

### Personalizar Logo

1. Coloca tu logo en: `static/logo.png`
2. Formato: PNG (fondo transparente recomendado)
3. Tamaño: 200x50 píxeles

## 🐛 Solución de Problemas

### Error: "Python no está instalado"
- Descarga Python desde: https://www.python.org/downloads/
- Durante la instalación, marca "Add Python to PATH"

### Error: "pip no se reconoce"
```bash
python -m pip install -r requirements.txt
```

### Error al generar PDF
- Verifica que WeasyPrint esté instalado correctamente
- En Windows, puede requerir GTK3: https://weasyprint.readthedocs.io/en/stable/install.html

### El logo no aparece
- Verifica que el archivo sea `static/logo.png`
- Formato debe ser PNG, JPG o GIF
- Tamaño recomendado: máximo 50px de altura

## 📚 Documentación Adicional

- [Guía Rápida](GUIA_RAPIDA.md) - Inicio rápido y uso básico
- [Instalación en Nuevo Equipo](INSTALACION_NUEVO_EQUIPO.txt) - Guía completa de instalación
- [Ejemplos de Uso](EJEMPLOS_USO.md) - Casos de uso prácticos
- [Checklist](CHECKLIST.txt) - Lista de verificación

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- **Laboratorios Novaderma S.A.** - Desarrollo inicial

## 🙏 Agradecimientos

- Flask por el excelente framework web
- WeasyPrint por la generación de PDFs
- openpyxl por el procesamiento de Excel

## 📞 Soporte

Para soporte técnico o preguntas:
- Abre un issue en GitHub
- Contacta al equipo de desarrollo

## 🔄 Changelog

### v1.0.0 (2026-02-11)
- ✨ Lanzamiento inicial
- ✅ Carga de archivos Excel
- ✅ Generación de PDFs
- ✅ Interfaz web moderna
- ✅ Clasificación automática de rendimiento

---

Hecho con ❤️ por Laboratorios Novaderma S.A.
