# Aplicativo para Depuración y Conversión de GLC a Forma Normal de Chomsky (FNC)

**Universidad Francisco de Paula Santander (UFPS)**  
**Teoría de la Computación 2026/02 - Microproyecto #1**

---

## 📌 Descripción General
Aplicativo desarrollado en **Python** que permite ingresar una **Gramática Libre de Contexto (GLC)** formalmente definida como $G = (V, T, P, S)$, validar sus componentes y realizar de forma automática o paso a paso el proceso completo de depuración y transformación hasta obtener una gramática equivalente en **Forma Normal de Chomsky (FNC)**.

El sistema registra y expone cada transformación intermedia, indicando claramente:
- Gramática inicial de la etapa.
- Elementos identificados (variables anulables, pares unitarios, variables no generadoras, inalcanzables, etc.).
- Reglas de producción eliminadas.
- Reglas de producción agregadas.
- Gramática resultante de cada fase.

---

## 🚀 Etapas del Proceso de Conversión
1. **Validación Inicial de la GLC**:
   - Existencia de variables, terminales y símbolo inicial.
   - Pertenencia del símbolo inicial al conjunto de variables ($S \in V$).
   - Detección de símbolos no declarados en las producciones.
   - Integridad sintáctica de cada regla de producción.
2. **Eliminación de Producciones Nulas ($A \to \varepsilon$)**:
   - Identificación del conjunto de variables anulables ($V_{null}$).
   - Sustitución combinatoria de variables anulables y remoción de $\varepsilon$.
3. **Eliminación de Producciones Unitarias ($A \to B$)**:
   - Determinación de pares unitarios y cálculo de la clausura unitaria.
   - Sustitución de producciones directas por producciones efectivas.
4. **Eliminación de Variables Inútiles**:
   - **Identificación de variables generadoras**: Eliminación de variables y reglas que no producen cadenas de terminales.
   - **Identificación de variables alcanzables**: Búsqueda en anchura/profundidad desde el símbolo inicial $S$ y eliminación de variables inaccesibles.
5. **Conversión a Forma Normal de Chomsky (FNC)**:
   - **Sustitución de terminales**: En producciones de longitud $\ge 2$, los terminales se reemplazan por variables auxiliares ($X_a \to a$).
   - **Reducción de producciones largas**: Producciones con más de 2 no terminales se binarizan utilizando nuevas variables auxiliares ($X_1, X_2, \dots$).
6. **Validación Automática FNC**:
   - Verificación estricta de que todas las reglas cumplan $A \to BC$ o $A \to a$.

---

## 📁 Estructura del Proyecto
```text
├── src/
│   ├── models/            # Modelos de datos (Grammar, Production, Symbol)
│   ├── parser/            # Validador y parser de gramáticas
│   ├── algorithms/        # Algoritmos de transformación (Null, Unit, Useless, Chomsky)
│   ├── history/           # Trazabilidad e historial paso a paso
│   └── ui/                # Menú interactivo y vistas por consola
├── tests/                 # Batería de pruebas unitarias con pytest/unittest
├── gramaticas_ejemplo/    # Archivos de gramáticas de prueba
├── docs/                  # Documento técnico y Manual de usuario
├── main.py                # Punto de entrada de la aplicación
├── requirements.txt       # Dependencias (si aplica)
└── README.md              # Documentación general
```

---

## 💻 Requisitos y Ejecución
- **Python 3.8+**
- Ejecución principal:
  ```bash
  python main.py
  ```

---

## 👥 Integrantes
- Estudiantes de Teoría de la Computación - UFPS
