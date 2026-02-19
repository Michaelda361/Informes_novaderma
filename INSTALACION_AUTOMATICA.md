# 🚀 Instalación Automática

## ⚡ Instalación Rápida (Recomendado)

### Windows
1. **Descarga** el proyecto completo
2. **Haz doble clic** en: `instalar_todo.bat`
3. **Espera** 5-10 minutos mientras se instala todo
4. **Instala GTK3** cuando el script abra el navegador
5. **Reinicia** tu computadora
6. **Ejecuta** `iniciar.bat` para iniciar la aplicación

---

## 📋 Qué Instala Automáticamente

El script `instalar_todo.bat` instala:

✅ **Python 3.11.9** - Lenguaje de programación (compatible con WeasyPrint)
✅ **pip** - Gestor de paquetes de Python
✅ **Flask 3.0.0** - Framework web
✅ **WeasyPrint 61.2** - Generador de PDFs
✅ **openpyxl 3.1.2** - Procesador de archivos Excel
✅ **Pillow 10.4.0** - Procesamiento de imágenes
✅ **Gunicorn 23.0.0** - Servidor de producción

⚠️ **GTK3 Runtime** - Debe instalarse manualmente (OBLIGATORIO para PDFs)

---

## 🔧 Instalación Manual (Alternativa)

Si prefieres instalar paso a paso:

### 1. Instalar Python 3.11
- **Descarga:** https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
- **Versión:** 3.11.9 (IMPORTANTE: No usar 3.12 o 3.13)
- ⚠️ **CRÍTICO:** Marca la casilla "Add Python to PATH"

### 2. Instalar Dependencias
Abre CMD o PowerShell en la carpeta del proyecto:
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Instalar GTK3 Runtime (OBLIGATORIO)
- **Descarga:** https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
- **Archivo:** `gtk3-runtime-x.x.x-x-x-x-ts-win64.exe` (el más reciente)
- **Ejecuta** el instalador como administrador
- **Acepta** todas las opciones por defecto
- **Reinicia** tu computadora después de instalar

---

## ▶️ Iniciar la Aplicación

### Método 1: Script Automático (Recomendado)
Haz doble clic en: **`iniciar.bat`**

El navegador se abrirá automáticamente en http://localhost:5000

### Método 2: Línea de Comandos
```bash
python app.py
```
Luego abre tu navegador en: **http://localhost:5000**

---

## 🔍 Verificar Instalación

Abre CMD o PowerShell y ejecuta:

```bash
# Verificar Python
python --version
# Debe mostrar: Python 3.11.9

# Verificar dependencias
python -c "import flask; print('Flask OK')"
python -c "import openpyxl; print('openpyxl OK')"
python -c "import weasyprint; print('WeasyPrint OK')"
python -c "import PIL; print('Pillow OK')"

# Si todos muestran "OK", la instalación es correcta
```

---

## ⚠️ Solución de Problemas

### "Python no se reconoce como comando"
**Causa:** Python no está en el PATH
**Solución:**
1. Cierra TODAS las ventanas de CMD/PowerShell
2. Abre una nueva ventana
3. Si persiste, reinstala Python marcando "Add Python to PATH"
4. Reinicia tu computadora

### "Error al generar PDF" o "OSError: cannot load library 'gobject-2.0-0'"
**Causa:** GTK3 no está instalado
**Solución:**
1. Instala GTK3 Runtime (ver paso 3 arriba)
2. Reinicia tu computadora
3. Ejecuta `iniciar.bat` de nuevo

### "pip no se reconoce como comando"
**Solución:**
```bash
python -m pip install -r requirements.txt
```

### "ModuleNotFoundError: No module named 'flask'"
**Causa:** Las dependencias no se instalaron
**Solución:**
```bash
python -m pip install -r requirements.txt
```

### La aplicación no abre el navegador
**Solución:**
Abre manualmente: http://localhost:5000

---

## 🐧 Instalación en Linux

### Ubuntu/Debian
```bash
# Instalar Python y dependencias del sistema
sudo apt update
sudo apt install python3.11 python3-pip python3-dev
sudo apt install libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0
sudo apt install libffi-dev shared-mime-info

# Instalar dependencias de Python
pip3 install -r requirements.txt

# Iniciar aplicación
python3 app.py
```

### Fedora/RHEL
```bash
sudo dnf install python3.11 python3-pip
sudo dnf install pango gdk-pixbuf2 libffi-devel
pip3 install -r requirements.txt
python3 app.py
```

---

## 🍎 Instalación en macOS

```bash
# Instalar Homebrew (si no lo tienes)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python 3.11
brew install python@3.11

# Instalar dependencias del sistema
brew install cairo pango gdk-pixbuf libffi

# Instalar dependencias de Python
pip3 install -r requirements.txt

# Iniciar aplicación
python3 app.py
```

---

## ✅ Checklist de Instalación

Antes de usar la aplicación, verifica:

- [ ] Python 3.11.9 instalado
- [ ] `python --version` muestra Python 3.11.x
- [ ] `pip --version` funciona
- [ ] Todas las dependencias instaladas (`pip list`)
- [ ] GTK3 Runtime instalado (solo Windows)
- [ ] Computadora reiniciada después de instalar GTK3
- [ ] `python app.py` inicia sin errores
- [ ] http://localhost:5000 abre correctamente
- [ ] Puedes cargar un archivo Excel
- [ ] Puedes generar un PDF de prueba

---

## 📞 Soporte

Si tienes problemas:

1. **Revisa** la sección "Solución de Problemas" arriba
2. **Verifica** el checklist de instalación
3. **Ejecuta** `python app.py` y revisa los mensajes de error
4. **Asegúrate** de tener Python 3.11 (no 3.12 o 3.13)

---

## 🔄 Actualizar el Proyecto

Si ya tienes el proyecto instalado y quieres actualizarlo:

```bash
# Actualizar código
git pull

# Actualizar dependencias
python -m pip install -r requirements.txt --upgrade

# Reiniciar aplicación
python app.py
```
