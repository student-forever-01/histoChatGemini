from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv  # Importar la función para cargar variables de entorno
import os  # Para acceder a las variables de entorno

# Cargar variables de entorno desde .env
load_dotenv()

app = Flask(__name__)

# Configura la API de Google Generative AI usando la clave del archivo .env
genai.configure(api_key=os.getenv("API_KEY"))

# Listado de personajes precargados
PERSONAJES = [
    "Albert Einstein",
    "Cleopatra",
    "Napoleón",
    "Marie Curie",
    "Mahatma Gandhi",
    "Leonardo da Vinci",
    "Frida Kahlo",
    "Winston Churchill",
    "Isaac Newton",
    "Martin Luther King Jr."
]

@app.route("/")
def home():
    return render_template("index.html", personajes=PERSONAJES)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    pregunta = data.get("pregunta")
    personaje = data.get("personaje")

    # Validar que el personaje no esté vacío
    if not personaje or not personaje.strip():
        return jsonify({"respuesta": "Error: Debes seleccionar o escribir un personaje válido."})

    # Validar que la pregunta no esté vacía
    if not pregunta or not pregunta.strip():
        return jsonify({"respuesta": "Error: Debes escribir una pregunta."})

    try:
        # Configurar el prompt para que Gemini responda como el personaje
        prompt = f"Responde la siguiente pregunta como si fueras {personaje}: {pregunta}"
        client = genai.GenerativeModel("gemini-2.0-flash")
        response = client.generate_content(prompt)
        return jsonify({"respuesta": f"{response.text}"})
    except Exception as e:
        return jsonify({"respuesta": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)