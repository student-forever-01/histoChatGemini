Chat con Personajes Históricos
Esta aplicación web permite a los usuarios interactuar con un chatbot que simula ser personajes históricos influyentes. Utiliza la API de Google Generative AI (Gemini) para generar respuestas en tiempo real, imitando el estilo y conocimiento de figuras como Albert Einstein, Cleopatra, Napoleón, Marie Curie, entre otros.

Características principales
Selección de personajes: Elige entre una lista precargada de 10 personajes históricos o escribe manualmente el nombre de otro personaje.

Respuestas contextuales: El chatbot responde como si fuera el personaje seleccionado, utilizando un formato claro y estructurado.

Interfaz moderna: Diseño responsivo y fácil de usar, construido con Flask (backend) y Bootstrap (frontend).

Seguridad: Las claves de API se gestionan de forma segura mediante variables de entorno y no se suben al repositorio.

Tecnologías utilizadas
Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript, Bootstrap

API: Google Generative AI (Gemini)

Herramientas: python-dotenv para gestión de variables de entorno

Cómo usar
Clona el repositorio.

Instala las dependencias: pip install -r requirements.txt.

Crea un archivo .env y agrega tu clave de API de Google Generative AI.

Ejecuta la aplicación: python app.py.

Abre tu navegador y visita http://127.0.0.1:5000.

Requisitos
Python 3.x

Clave de API de Google Generative AI
