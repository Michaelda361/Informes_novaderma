# 🔧 Solución de Problemas en Render

## Cambios Aplicados

He agregado/actualizado estos archivos para solucionar el problema:

1. **apt-packages.txt** - Instala dependencias del sistema para WeasyPrint
2. **requirements.txt** - Versiones actualizadas y compatibles
3. **render.yaml** - Configuración mejorada del build
4. **runtime.txt** - Fuerza Python 3.11.9

## 📋 Pasos para Aplicar la Solución

### Opción A: Subir los cambios (Recomendado)

```bash
git add .
git commit -m "Fix: Agregar dependencias del sistema para WeasyPrint"
git push
```

Render detectará los cambios y volverá a desplegar automáticamente.

### Opción B: Configuración Manual en Render

Si sigue fallando, configura manualmente:

1. **Ve a tu servicio en Render**
2. **Settings** → **Build & Deploy**
3. **Build Command:**
   ```
   pip install --upgrade pip setuptools wheel && pip install -r requirements.txt
   ```
4. **Start Command:**
   ```
   gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
   ```
5. **Environment** → Agrega:
   - `PYTHON_VERSION` = `3.11.9`

6. **Manual Deploy** → Click en "Clear build cache & deploy"

---

## 🐛 Errores Comunes y Soluciones

### Error: "Failed to build Pillow"
**Causa:** Python 3.14 es muy nuevo
**Solución:** Usar Python 3.11.9 (ya configurado en runtime.txt)

### Error: "cairo library not found"
**Causa:** Faltan dependencias del sistema para WeasyPrint
**Solución:** El archivo apt-packages.txt las instala automáticamente

### Error: "No module named 'cffi'"
**Causa:** Falta dependencia de WeasyPrint
**Solución:** Ya agregado en requirements.txt

### Error: "Worker timeout"
**Causa:** El servidor tarda mucho en responder
**Solución:** Aumentar timeout en gunicorn (ya configurado: --timeout 120)

---

## 🔍 Verificar los Logs

En Render dashboard:
1. Click en tu servicio
2. Pestaña "Logs"
3. Busca líneas que digan "ERROR" o "FAILED"
4. Copia el error completo

---

## 🚀 Alternativa: Railway.app

Si Render sigue dando problemas, Railway es más simple:

1. **Ve a:** https://railway.app
2. **Sign up** con GitHub
3. **New Project** → Deploy from GitHub repo
4. **Selecciona** tu repositorio
5. Railway lo despliega automáticamente (sin configuración)
6. **Settings** → Generate Domain
7. ¡Listo!

Railway tiene mejor soporte para WeasyPrint y no requiere configuración.

---

## 📊 Verificar que Funciona

Una vez desplegado, prueba:

1. Abre la URL de tu app
2. Sube un archivo Excel
3. Genera un PDF
4. Si funciona, ¡éxito! 🎉

---

## ⚠️ Si Nada Funciona

**Plan B: Usar Railway en lugar de Render**

Railway es más tolerante con dependencias complejas como WeasyPrint.

**Plan C: Simplificar el proyecto**

Si necesitas algo rápido, puedo ayudarte a:
- Usar una librería más simple para PDFs (reportlab)
- O generar HTML en lugar de PDF
- O usar un servicio externo para generar PDFs

---

## 📞 Necesitas Ayuda

Copia y pega el error completo de los logs de Render para que pueda ayudarte mejor.
