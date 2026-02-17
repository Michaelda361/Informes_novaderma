# 📊 Cálculo Automático de Promedios

El sistema calcula automáticamente el promedio de evaluación usando una lógica inteligente.

## 🔄 Lógica de Cálculo

### Prioridad 1: Usar Porcentaje del Excel

Si el archivo Excel tiene una columna de "PORCENTAJE" o "%" con un valor:

#### Escala 1-5 (Directa)
```
Porcentaje en Excel: 4.5
Promedio calculado: 4.5
```

#### Escala 0-100 (Conversión automática)
```
Porcentaje en Excel: 85%
Conversión: 85 / 100 * 5 = 4.25
Promedio calculado: 4.25
```

### Prioridad 2: Calcular de Calificaciones

Si NO hay porcentaje en el Excel, el sistema:

1. **Busca todas las calificaciones** (valores entre 1 y 5)
2. **Calcula el promedio** de todas ellas
3. **Redondea** a 2 decimales

```
Calificaciones: [4, 5, 4, 5, 4, 3, 5]
Promedio: (4+5+4+5+4+3+5) / 7 = 4.29
```

### Prioridad 3: Sin Datos

Si no hay porcentaje ni calificaciones:
```
Promedio: 0.00
Rendimiento: Deficiente
```

---

## 📋 Ejemplos Prácticos

### Ejemplo 1: Excel con Porcentaje
```
Columna "PORCENTAJE": 4.5
Resultado: Promedio = 4.5, Rendimiento = Satisfactorio
```

### Ejemplo 2: Excel sin Porcentaje
```
Calificaciones encontradas: 4, 5, 4, 5, 4, 4, 5, 4, 5, 4
Promedio calculado: 4.4
Resultado: Promedio = 4.4, Rendimiento = Satisfactorio
```

### Ejemplo 3: Excel con Porcentaje en %
```
Columna "PORCENTAJE": 90
Conversión: 90/100 * 5 = 4.5
Resultado: Promedio = 4.5, Rendimiento = Satisfactorio
```

---

## 🎯 Clasificación del Rendimiento

Una vez calculado el promedio, se clasifica automáticamente:

| Promedio | Clasificación |
|----------|---------------|
| 4.5 - 5.0 | Sobresaliente |
| 3.5 - 4.4 | Satisfactorio |
| 2.5 - 3.4 | Aceptable |
| 1.5 - 2.4 | No Satisfactorio |
| 0.0 - 1.4 | Deficiente |

---

## ✅ Ventajas

1. **Flexible:** Funciona con o sin columna de porcentaje
2. **Inteligente:** Detecta automáticamente la escala (1-5 o 0-100)
3. **Robusto:** Maneja casos sin datos
4. **Preciso:** Redondea a 2 decimales

---

## 🔧 Columnas Buscadas

El sistema busca estas columnas para el porcentaje:
- "PORCENTAJE"
- "%"
- "PUNTAJE TOTAL"
- "Porcentaje de cumplimiento"

Si no encuentra ninguna, calcula automáticamente.

---

## 📝 Notas Técnicas

- El cálculo se hace en tiempo real al procesar el Excel
- No modifica el archivo Excel original
- El promedio se guarda en el objeto de evaluación
- Se usa para generar el PDF y mostrar en la interfaz

---

## 🧪 Casos de Prueba

Todos los casos han sido probados:

✅ Con porcentaje en escala 1-5
✅ Con porcentaje en escala 0-100
✅ Sin porcentaje (cálculo automático)
✅ Sin datos (promedio = 0)

---

## 💡 Recomendación

Para mejores resultados:
- Incluye la columna "PORCENTAJE" en tu Excel
- O asegúrate de que todas las calificaciones estén completas
- Las calificaciones deben estar entre 1 y 5
