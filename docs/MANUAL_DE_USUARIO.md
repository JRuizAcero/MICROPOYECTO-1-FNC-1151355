# MANUAL DE USUARIO

**APLICATIVO PARA DEPURACIÓN Y CONVERSIÓN DE GLC A FORMA NORMAL DE CHOMSKY**

---

## 1. PRESENTACIÓN DEL SISTEMA
El **Aplicativo para Depuración y Conversión de Gramáticas Libres de Contexto a Forma Normal de Chomsky** es una herramienta de software diseñada para estudiantes y docentes de Teoría de la Computación. Permite ingresar cualquier Gramática Libre de Contexto (GLC) $G = (V, T, P, S)$, verificar que esté correctamente definida y transformarla paso a paso o de manera totalmente automática a su equivalente en **Forma Normal de Chomsky (FNC)**.

El sistema destaca por su transparencia didáctica: en cada fase del proceso muestra las variables identificadas, las reglas de producción eliminadas, las reglas agregadas y la gramática intermedia resultante.

---

## 2. REQUISITOS DEL SISTEMA
Para ejecutar este aplicativo se requiere:
- **Sistema Operativo:** Windows 10/11, Linux o macOS.
- **Entorno de ejecución:** **Python 3.8** o superior (probado y certificado en Python 3.12).
- **Librerías externas:** Ninguna (utiliza la biblioteca estándar de Python, garantizando portabilidad total sin necesidad de `pip install`).

---

## 3. INSTALACIÓN Y EJECUCIÓN PASO A PASO

1. **Descargar o clonar el repositorio:**
   ```bash
   git clone https://github.com/JulianGomezIbarra/MICROPOYECTO-1-FNC-1151355.git
   ```
2. **Navegar a la carpeta del proyecto:**
   ```bash
   cd "MICROPOYECTO 1 FNC-1151355"
   ```
3. **Iniciar el aplicativo:**
   ```bash
   python main.py
   ```
   *(En algunos sistemas Windows puede utilizarse `py main.py`)*.

---

## 4. INGRESO DE UNA GRAMÁTICA (OPCIÓN 1)
Al seleccionar la opción **1** del menú principal, dispondrá de 3 modalidades de ingreso:

### Modalidad 1: Ingreso Manual Guiado
El sistema le solicitará secuencialmente:
1. **Variables no terminales ($V$):** Ingréselas separadas por comas o espacios.
   - *Ejemplo:* `S, A, B, C`
2. **Símbolos terminales ($T$):** Ingréselos separados por comas o espacios.
   - *Ejemplo:* `a, b, c`
3. **Símbolo inicial ($S$):** Ingrese la variable inicial.
   - *Ejemplo:* `S`
4. **Reglas de producción ($P$):** Ingrese las producciones una a una. 
   - Puede usar la barra vertical `|` para agrupar alternativas.
   - Para la cadena vacía $\varepsilon$, puede escribir `ε`, `epsilon` o `lambda`.
   - *Ejemplo:* `S -> AB | a | ε`
   - Cuando termine de ingresar reglas, escriba `FIN` o presione Enter en una línea en blanco.

### Modalidad 2: Cargar Gramática de Prueba
El sistema incluye 3 gramáticas clásicas listas para usar:
- **Ejemplo 1:** Gramática completa de Chomsky con recursión mutua.
- **Ejemplo 2:** Gramática con variables anulables directas e indirectas.
- **Ejemplo 3:** Gramática con variables no generadoras e inalcanzables.

### Modalidad 3: Pegar en Bloque de Texto
Permite copiar y pegar directamente la definición formal en bloque:
```text
Variables: S, A, B
Terminales: a, b
Inicial: S
Producciones:
S -> aB | bA
A -> a | aS | bAA
B -> b | bS | aBB
FIN
```

---

## 5. VALIDACIÓN DE LA GRAMÁTICA (OPCIÓN 3)
Antes de realizar transformaciones, el sistema evalúa la gramática con la opción **3**:
- Verifica que existan variables y terminales.
- Valida que el símbolo inicial pertenezca a $V$.
- Comprueba que ningún símbolo terminal esté declarado como variable ni viceversa ($V \cap T = \emptyset$).
- Detecta símbolos no declarados en el lado derecho de las producciones.
- Si todo es correcto, muestra el mensaje: `[OK] La gramática es VÁLIDA y cumple con todos los requisitos formales.`

---

## 6. EJECUCIÓN PASO A PASO (OPCIONES 4 A 8)
El usuario puede ejecutar de forma individual e interactiva cada procedimiento:

- **Opción 4 - Eliminar producciones nulas:**
  Identifica variables anulables ($V_{null}$), genera las combinaciones sin $\varepsilon$ y elimina las reglas $A \to \varepsilon$.
- **Opción 5 - Eliminar producciones unitarias:**
  Calcula los pares unitarios $(A, B)$ por transitividad y sustituye las reglas unitarias $A \to B$ por producciones terminales o compuestas directas.
- **Opción 6 - Eliminar variables inútiles (no generadoras):**
  Identifica inductivamente las variables que pueden derivar en cadenas de terminales y poda aquellas que no lo logran.
- **Opción 7 - Eliminar variables inalcanzables:**
  Aplica un recorrido en anchura desde el símbolo inicial $S$ y elimina cualquier variable que haya quedado aislada.
- **Opción 8 - Convertir a Forma Normal de Chomsky:**
  Sustituye terminales en producciones compuestas ($X_a \to a$) y binariza producciones de más de dos variables ($X_1, X_2, \dots$).

---

## 7. EJECUCIÓN AUTOMÁTICA (OPCIÓN 9)
La opción **9** ejecuta en una sola acción todo el pipeline de transformación en el orden canónico riguroso:
1. Validación formal.
2. Eliminación de nulas.
3. Eliminación de unitarias.
4. Eliminación de no generadoras.
5. Eliminación de inalcanzables.
6. Sustitución de terminales en producciones largas.
7. Binarización de producciones $> 2$.
8. Verificación automática final de FNC.

---

## 8. INTERPRETACIÓN DE RESULTADOS
Cada reporte emitido por el sistema contiene 4 secciones estandarizadas:

1. **Elementos identificados:** Muestra qué componentes teóricos detectó el algoritmo (ej. `{ A, B }` en anulables, o `{ (S =>* A) }` en pares unitarios).
2. **Producciones eliminadas:** Prefijadas con `[-]`, corresponden a las reglas que violan la restricción de la etapa y fueron suprimidas.
3. **Producciones agregadas:** Prefijadas con `[+]`, corresponden a las nuevas reglas generadas para conservar el lenguaje sin la restricción eliminada.
4. **Gramática resultante:** Muestra la tupla formal $G = (V, T, P, S)$ tras aplicar la transformación.

---

## 9. MENSAJES DE ERROR MÁS FRECUENTES Y SOLUCIÓN

| Mensaje de Error | Causa | Solución |
| :--- | :--- | :--- |
| `Error: El símbolo inicial 'X' no pertenece al conjunto de variables` | El símbolo inicial escrito no fue incluido en la lista de variables. | Agregue `X` a la lista de variables no terminales. |
| `Error en producción S -> AD: La variable 'D' no fue declarada en V` | Se utilizó un símbolo en mayúscula que no se declaró previamente. | Declare la variable `D` en el conjunto $V$ o corrija el nombre. |
| `Error: Conflicto entre variables y terminales` | Un mismo símbolo fue ingresado simultáneamente en $V$ y en $T$. | Recuerde que $V \cap T = \emptyset$. Separe claramente variables (usualmente mayúsculas) y terminales (minúsculas). |
| `No hay ninguna gramática registrada` | Se intentó ejecutar una transformación sin haber ingresado una gramática. | Utilice la opción 1 para cargar o ingresar una gramática primero. |

---

## 10. EJEMPLO COMPLETO ILUSTRADO

### Entrada de la Gramática
```text
Variables: S, A, B
Terminales: a, b
Inicial: S
Producciones:
S -> aB | bA
A -> a | aS | bAA
B -> b | bS | aBB
```

### Ejecución Automática (Opción 9)
El sistema informa:
- Nulas identificadas: ninguna.
- Unitarias identificadas: ninguna.
- Variables no generadoras: ninguna.
- Variables inalcanzables: ninguna.
- Terminales en reglas compuestas sustituidos:
  - `a -> X1` con regla `X1 -> a`
  - `b -> X2` con regla `X2 -> b`
- Reglas binarizadas:
  - `A -> X2 A A` descompuesta en `A -> X2 X3` y `X3 -> AA`
  - `B -> X1 B B` descompuesta en `B -> X1 X4` y `X4 -> BB`

### Gramática Resultante en FNC
```text
V = { A, B, S, X1, X2, X3, X4 }
T = { a, b }
S = S
P = {
    S -> X2 A | X1 B
    A -> X1 S | a | X2 X3
    B -> X2 S | X1 X4 | b
    X1 -> a
    X2 -> b
    X3 -> AA
    X4 -> BB
}
```

### Resultado de la Validación Automática:
```text
[EXITO] VERIFICACION EXITOSA: La gramatica resultante se encuentra estrictamente en Forma Normal de Chomsky (FNC).
  Todas las producciones cumplen con el formato A -> BC (con B, C en V) o A -> a (con a en T).
```
