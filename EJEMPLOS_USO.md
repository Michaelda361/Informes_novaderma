# 📚 Ejemplos de Uso

## Caso 1: Generar un solo reporte

1. Inicia la aplicación con `iniciar.bat`
2. Abre http://localhost:5000
3. Arrastra tu archivo Excel
4. Busca la evaluación que necesitas
5. Haz clic en "📄 Generar PDF"
6. El PDF se descarga automáticamente

**Tiempo estimado:** 10 segundos

---

## Caso 2: Generar todos los reportes

1. Inicia la aplicación
2. Carga el archivo Excel
3. Haz clic en "📥 Descargar Todos los PDF"
4. Espera a que se descarguen todos (uno por uno)

**Tiempo estimado:** 5-10 segundos por reporte

---

## Caso 3: Revisar evaluaciones antes de generar PDF

1. Carga el archivo Excel
2. Revisa la tabla con todas las evaluaciones:
   - Nombre del colaborador
   - Cargo y área
   - Promedio obtenido
   - Clasificación de rendimiento
3. Genera solo los PDFs que necesites

---

## Caso 4: Procesar múltiples archivos Excel

1. Carga el primer archivo Excel
2. Genera los PDFs necesarios
3. Recarga la página (F5)
4. Carga el siguiente archivo Excel
5. Repite el proceso

**Nota:** Los PDFs se guardan con nombres únicos, no se sobrescriben

---

## Caso 5: Personalizar el logo

### Antes de iniciar:
1. Coloca tu logo en: `static/logo.png`
2. Inicia la aplicación
3. Los PDFs incluirán el logo automáticamente

### Si ya está corriendo:
1. Detén el servidor (Ctrl+C)
2. Agrega el logo en `static/logo.png`
3. Reinicia con `iniciar.bat`

---

## Interpretación de Resultados

### Tabla de Evaluaciones

| Columna | Descripción |
|---------|-------------|
| **ID** | Identificador único de la evaluación |
| **Nombre** | Nombre del colaborador evaluado |
| **Cargo** | Puesto del colaborador |
| **Área** | Departamento o área de trabajo |
| **Promedio** | Calificación promedio (1-5) |
| **Rendimiento** | Clasificación según promedio |

### Clasificación de Rendimiento

| Badge | Promedio | Significado |
|-------|----------|-------------|
| 🟢 **Sobresaliente** | ≥ 4.5 | Desempeño excepcional |
| 🔵 **Satisfactorio** | 3.5 - 4.49 | Cumple expectativas |
| 🟠 **Aceptable** | 2.5 - 3.49 | Necesita mejoras menores |
| 🔴 **No Satisfactorio** | 1.5 - 2.49 | Requiere plan de mejora |
| ⚫ **Deficiente** | < 1.5 | Requiere acción inmediata |

---

## Contenido del PDF Generado

Cada PDF incluye:

### 1. Encabezado
- Logo de la empresa
- Código del formato (FT-RH-042)
- Versión y vigencia

### 2. Datos del Colaborador
- Nombre completo
- Cargo y área
- Jefe inmediato
- Período evaluado
- Fecha de evaluación

### 3. Resumen de Desempeño
- Promedio general
- Clasificación de rendimiento
- Comentarios del jefe inmediato

### 4. Calificaciones Detalladas
- Desempeño operativo (4 criterios)
- Compromiso y calidad (3 criterios)
- Comportamiento y trabajo en equipo (3 criterios)

### 5. Información Cualitativa
- Aportes del colaborador
- Plan de mejora propuesto

### 6. Pie de Página
- Nota sobre el uso del formato
- Referencia al Sistema de Gestión de Calidad

---

## Tips y Mejores Prácticas

### ✅ Hacer

- Cierra el archivo Excel antes de cargarlo
- Usa navegadores modernos (Chrome, Edge, Firefox)
- Verifica los datos en la tabla antes de generar PDFs
- Guarda los PDFs en una carpeta organizada
- Mantén una copia de seguridad del Excel original

### ❌ Evitar

- No modifiques el Excel mientras está cargado
- No cierres la terminal mientras usas la app
- No cambies la estructura de columnas del Excel
- No uses caracteres especiales en nombres de archivo
- No intentes cargar archivos muy grandes (>16MB)

---

## Atajos de Teclado

| Atajo | Acción |
|-------|--------|
| **F5** | Recargar página |
| **Ctrl+C** | Detener servidor (en terminal) |
| **Ctrl+Clic** | Abrir PDF en nueva pestaña |

---

## Preguntas Frecuentes

### ¿Puedo editar el PDF después de generarlo?
No directamente. Debes modificar el Excel y regenerar el PDF.

### ¿Los PDFs se guardan automáticamente?
Sí, en la carpeta `output/` y también se descargan al navegador.

### ¿Puedo cambiar el diseño del PDF?
Sí, editando el archivo `templates/reporte.html`.

### ¿Cuántos reportes puedo generar?
Ilimitados. Solo depende del espacio en disco.

### ¿Funciona sin internet?
Sí, es 100% local. No requiere conexión a internet.

---

## Ejemplos de Nombres de Archivo Generados

```
evaluacion_Wilson_22.pdf
evaluacion_Katherine_Quintana_Rueda_23.pdf
evaluacion_Valeria_echavarría_24.pdf
evaluacion_ANA_MARIA_DOMINGUEZ_SILVA_25.pdf
```

El formato es: `evaluacion_[Nombre]_[ID].pdf`

---

## Flujo de Trabajo Recomendado

```
1. Preparar Excel
   ↓
2. Iniciar aplicación (iniciar.bat)
   ↓
3. Cargar Excel en navegador
   ↓
4. Revisar tabla de evaluaciones
   ↓
5. Generar PDFs necesarios
   ↓
6. Organizar PDFs descargados
   ↓
7. Distribuir a colaboradores
```

---

## Soporte Adicional

Si necesitas ayuda adicional:
1. Revisa `GUIA_RAPIDA.md`
2. Consulta `README.md`
3. Verifica `INSTALACION.txt`
4. Contacta al equipo de desarrollo
