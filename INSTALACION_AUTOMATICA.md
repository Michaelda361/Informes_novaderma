# 🚀 Instalación Automática

## ⚡ Instalación Rápida (Recomendado)

### Windows
1. Haz doble clic en: **`instalar_todo.bat`**
2. Espera 5-10 minutos
3. Instala GTK3 cuando te lo pida
4. ¡Listo!

---

## 📋 Qué Instala

El script `instalar_todo.bat` instala automáticamente:

✅ **Python 3.11.9** - Lenguaje de programación
✅ **Flask** - Framework web
✅ **WeasyPrint** - Generador de PDFs
✅ **openpyxl** - Procesador de Excel
✅ **Pillow** - Procesamiento de imágenes
✅ **Gunicorn** - Servidor de producción

⚠️ **GTK3 Runtime** - Debe instalarse manualmente (el script abre la página)

---

## 🔧 Instalación Manual

Si prefieres instalar manualmente:

### 1. Instalar Python
- Descarga: https://www.python.org/downloads/
- Versión: 3.11 o superior
- ⚠️ **IMPORTANTE:** Marca "Add Python to PATH"

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 3. Instalar GTK3 (Solo Windows)
- Descarga: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
- Ejecuta el instalador `.exe`

---

## ▶️ Iniciar la Aplicación

### Opción A: Script
Haz doble clic en: **`iniciar.bat`**

### Opción B: Comando
```bash
python app.py
```

Abre tu navegador en: **http://localhost:5000**

---

## 🔍 Verificar Instalación

```bash
python --version
# Debe mostrar: Python 3.11.x o superior

pip list
# Debe mostrar: Flask, openpyxl, WeasyPrint, Pillow
```

---

## ⚠️ Solución de Problemas

### "Python no se reconoce"
1. Cierra TODAS las terminales
2. Abre una nueva terminal
3. Si persiste, reinstala Python marcando "Add to PATH"

### "Error al generar PDF"
- Instala GTK3 Runtime (ver paso 3 arriba)

### "pip no se reconoce"
```bash
python -m pip install -r requirements.txt
```

---

## 🌐 Instalación en Linux/Mac

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install python3.11 python3-pip
pip3 install -r requirements.txt
```

### macOS
```bash
brew install python@3.11
pip3 install -r requirements.txt
```

---

## ✅ Checklist

- [ ] Python 3.11+ instalado
- [ ] `python --version` funciona
- [ ] Dependencias instaladas
- [ ] GTK3 instalado (Windows)
- [ ] `python app.py` inicia sin errores
- [ ] http://localhost:5000 funciona
