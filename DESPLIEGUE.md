# Guía de Despliegue Gratuito

## Opción 1: Render.com (Recomendado)

### Pasos:

1. **Sube tu código a GitHub**
   - Crea un repositorio en GitHub
   - Sube todos los archivos del proyecto

2. **Crea una cuenta en Render**
   - Ve a https://render.com
   - Regístrate gratis con tu cuenta de GitHub

3. **Crea un nuevo Web Service**
   - Click en "New +" → "Web Service"
   - Conecta tu repositorio de GitHub
   - Render detectará automáticamente el `render.yaml`

4. **Configura el servicio**
   - Name: `informes-novaderma`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Plan: `Free`

5. **Despliega**
   - Click en "Create Web Service"
   - Espera 5-10 minutos mientras se despliega
   - Tu app estará disponible en: `https://informes-novaderma.onrender.com`

### Ventajas:
- ✅ Totalmente gratis (750 horas/mes)
- ✅ SSL automático (HTTPS)
- ✅ Despliegue automático cuando haces push a GitHub
- ✅ Soporta WeasyPrint sin configuración extra

### Desventajas:
- ⚠️ Se "duerme" después de 15 minutos sin uso (tarda ~30 segundos en despertar)

---

## Opción 2: Railway.app

### Pasos:

1. **Sube tu código a GitHub**

2. **Crea una cuenta en Railway**
   - Ve a https://railway.app
   - Regístrate con GitHub

3. **Crea un nuevo proyecto**
   - Click en "New Project"
   - Selecciona "Deploy from GitHub repo"
   - Elige tu repositorio

4. **Railway detectará automáticamente que es Flask**
   - No necesitas configurar nada más
   - Se desplegará automáticamente

5. **Genera un dominio público**
   - Ve a Settings → Generate Domain
   - Tu app estará disponible en: `https://tu-proyecto.up.railway.app`

### Ventajas:
- ✅ $5 de crédito gratis al mes
- ✅ No se duerme
- ✅ Muy rápido

### Desventajas:
- ⚠️ Crédito limitado ($5/mes)

---

## Opción 3: PythonAnywhere

### Pasos:

1. **Crea una cuenta**
   - Ve a https://www.pythonanywhere.com
   - Regístrate gratis

2. **Sube tu código**
   - Usa Git o sube archivos manualmente
   - O clona desde GitHub

3. **Configura la Web App**
   - Ve a "Web" → "Add a new web app"
   - Selecciona Flask
   - Configura el path a tu `app.py`

4. **Instala dependencias**
   - Abre una consola Bash
   - `pip install -r requirements.txt`

5. **Configura WeasyPrint** (requiere pasos adicionales)
   ```bash
   sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0
   ```

### Ventajas:
- ✅ Gratis permanente
- ✅ No se duerme

### Desventajas:
- ⚠️ Configuración más compleja
- ⚠️ Requiere configuración manual de WeasyPrint

---

## Recomendación Final

**Para este proyecto, usa Render.com** porque:
1. Es completamente gratis
2. Soporta WeasyPrint sin problemas
3. Despliegue automático desde GitHub
4. Configuración muy simple

---

## Archivos Necesarios (Ya incluidos)

- ✅ `requirements.txt` - Dependencias de Python
- ✅ `render.yaml` - Configuración para Render
- ✅ `app.py` - Tu aplicación Flask

---

## Notas Importantes

1. **Archivos grandes**: Los archivos Excel subidos se guardan en memoria temporal y se borran al reiniciar el servidor

2. **Variables de entorno**: Si necesitas configurar algo, puedes agregar variables de entorno en el dashboard de Render

3. **Logs**: Puedes ver los logs en tiempo real en el dashboard de Render para debugging

4. **Dominio personalizado**: Render permite conectar tu propio dominio gratis

---

## Solución de Problemas

### Si WeasyPrint falla en Render:
Render ya incluye las dependencias necesarias, pero si hay problemas, agrega un archivo `apt-packages.txt`:
```
libpango-1.0-0
libpangoft2-1.0-0
```

### Si la app se queda "dormida":
Es normal en el plan gratuito de Render. La primera petición después de 15 minutos tardará ~30 segundos.

### Si necesitas más recursos:
Considera actualizar al plan de pago ($7/mes) que incluye:
- No se duerme
- Más RAM y CPU
- Mejor rendimiento
