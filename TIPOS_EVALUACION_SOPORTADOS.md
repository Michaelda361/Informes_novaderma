# 📋 Tipos de Evaluación Soportados

El sistema procesa automáticamente los siguientes tipos de evaluaciones de desempeño:

## ✅ Tipos Soportados

### 1. OPERATIVO
- **Archivo:** EVALUACIÓN DE DESEMPEÑO OPERATIVO
- **Columnas:** 51
- **Características:**
  - Enfocado en tareas operativas y cumplimiento
  - Incluye "Porcentaje de error"
  - Evaluaciones de uso de equipos y procedimientos

### 2. DIRECTIVOS
- **Archivo:** EVALUACIÓN DE DESEMPEÑO DIRECTIVOS
- **Columnas:** 55
- **Características:**
  - Enfocado en liderazgo y gestión
  - Incluye "% Promedio de cumplimiento en los objetivos del cargo"
  - Evaluaciones de dirección de equipos y toma de decisiones

### 3. COMERCIAL
- **Archivo:** EVALUACIÓN DE DESEMPEÑO COMERCIAL
- **Columnas:** 55
- **Características:**
  - Enfocado en ventas y relaciones comerciales
  - Evaluaciones de cumplimiento de objetivos de ventas
  - Planificación y gestión de territorio

### 4. ADMINISTRATIVA
- **Archivo:** EVALUACIÓN DE DESEMPEÑO ADMINISTRATIVA
- **Columnas:** 50
- **Características:**
  - Enfocado en procesos administrativos
  - Incluye "Porcentaje de cumplimiento del plan de trabajo"
  - Evaluaciones de apoyo y soporte administrativo

---

## 🔄 Cómo Funciona

El sistema utiliza **búsqueda inteligente** que:

1. **Detecta automáticamente** las columnas por su nombre
2. **Se adapta** a diferentes órdenes de columnas
3. **Ignora** columnas faltantes o adicionales
4. **Normaliza** nombres con acentos, mayúsculas y espacios

### Columnas que Busca:

#### Datos Básicos:
- ID / Identificación
- Nombre / Nombre1
- Cargo / Puesto
- Área / Departamento
- Jefe inmediato / Supervisor
- Fecha de evaluación
- Período de evaluación

#### Calificaciones (1-5):
- Organización del trabajo
- Cumplimiento de resultados
- Aplicación de capacitaciones
- Uso de equipos
- Cumplimiento de políticas
- Conocimiento de calidad
- Propuestas de mejora
- Relaciones interpersonales
- Trabajo en equipo
- Actitud de servicio

#### Campos de Texto:
- Aportes realizados
- Aspectos a mejorar
- Debilidades identificadas
- Objetivos alcanzados
- Objetivos futuros
- Comentarios del jefe inmediato
- Plan de mejora propuesto

---

## 📊 Resultados del Procesamiento

Para cada evaluación, el sistema extrae:

```json
{
  "id": 18,
  "nombre": "ANTONIO MERCHAN",
  "cargo": "AUXILIAR DE ALMACEN",
  "area": "LOGISTICA",
  "jefe": "ROSALBA CORTES",
  "fecha": "2025/12/01",
  "periodo": "2025",
  "promedio": 3.97,
  "rendimiento": "Satisfactorio",
  "calificaciones": {
    "organizacion": 4,
    "cumple_resultados": 4,
    "aplica_capacitacion": 4,
    ...
  },
  "aportes": "CUMPLIMIENTO DE SGC",
  "comentario_jefe": "SE MANTIENE FIEL A LA COMPAÑIA",
  "plan_mejora": "RECORDACION DE PROCEDIMIENTOS DEL AREA"
}
```

---

## 🎯 Clasificación del Rendimiento

Basado en el promedio de calificaciones:

| Promedio | Clasificación |
|----------|---------------|
| 4.5 - 5.0 | Sobresaliente |
| 3.5 - 4.4 | Satisfactorio |
| 2.5 - 3.4 | Aceptable |
| 1.5 - 2.4 | No Satisfactorio |
| 0.0 - 1.4 | Deficiente |

---

## ✨ Ventajas del Sistema

1. **Flexible:** Se adapta a cambios en la estructura del Excel
2. **Robusto:** Maneja columnas faltantes o adicionales
3. **Inteligente:** Busca columnas por nombre, no por posición
4. **Universal:** Funciona con todos los tipos de evaluación

---

## 🔧 Agregar Nuevos Tipos

Si necesitas agregar un nuevo tipo de evaluación:

1. El sistema lo procesará automáticamente
2. Solo asegúrate de que tenga:
   - Columna de ID
   - Columna de Nombre
   - Calificaciones numéricas (1-5)
   - Columnas de texto con nombres similares

No se requiere modificar código.

---

## 📝 Notas Importantes

- Los archivos deben ser `.xlsx` o `.xls`
- La primera fila debe contener los encabezados
- Las calificaciones deben estar entre 1 y 5
- Los campos de texto pueden estar vacíos
- El sistema ignora filas sin ID

---

## ✅ Probado y Funcionando

Todos los tipos han sido probados exitosamente:

- ✅ OPERATIVO: 6 evaluaciones procesadas
- ✅ DIRECTIVOS: 9 evaluaciones procesadas
- ✅ COMERCIAL: 17 evaluaciones procesadas
- ✅ ADMINISTRATIVA: 13 evaluaciones procesadas

Total: 45 evaluaciones procesadas correctamente.
