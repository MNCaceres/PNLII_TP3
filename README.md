# TP3 - LLM con Razonamiento (FIUBA - PLN II)

## Consigna

> Implementar una aplicación que funcione como un **LLM con razonamiento**, el cual recibe una **pregunta compleja** y utiliza diferentes **agentes** para resolverla parcialmente, **compaginando todas las respuestas** para ofrecer una solución final.  
>
> Además de la respuesta, se debe imprimir la cantidad de **tokens de entrada**, **tokens de salida** y **tokens de razonamiento** (estos últimos son los utilizados en las etapas intermedias).
>
> **Entregables:**  
> • Link al repositorio ✅  
> • Video demostrativo ✅

---

## 📚 Descripción del proyecto

Esta aplicación permite interactuar con un modelo de lenguaje grande (LLM) para:

- Resolver **preguntas complejas** descomponiéndolas en pasos más simples.
- **Razonar** paso a paso utilizando datos explícitos entregados en el prompt.
- **Sumar los resultados parciales** para obtener una respuesta final.
- **Contabilizar** la cantidad de tokens de entrada, salida y razonamiento intermedio.

El proyecto cuenta con:
- **Una app de consola** (`main.py`) para consultas directas.
- **Una app web simple** (`app.py` + `index.html`) utilizando Flask.

---

## ⚙️ Tecnologías utilizadas

- Python 3.11
- OpenAI / Groq API (Modelos Llama3)
- Flask (para la versión web)
- Tiktoken (para contar tokens)

---


---

## 🚀 ¿Cómo correrlo?

### 1. Configurar variables de entorno

Crear un archivo `.env` con el siguiente contenido:

```bash
GROQ_API_KEY=tu_api_key



### 2. Instalar dependencias

pip install -r requirements.txt


### 3. Ejecutar modo consola

python src/main.py


### 4. Ejecutar modo web (opcional)

python src/app.py

Abrir navegador en http://127.0.0.1:5050/

