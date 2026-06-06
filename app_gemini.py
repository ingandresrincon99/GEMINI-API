import os 
from google import genai
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()   

clave_api = os.getenv("GEMINI_API_KEY")
cliente = genai.Client(api_key=clave_api)

def ejecutar_consulta():
    print("Ejecutando consulta a Gemini API...")

    try:
        respuesta = cliente.models.generate_content(
            model="gemini-3.5-flash",
            contents="Presetate como experto en machine learning y responde a esta pregunta: ¿Cuáles son las mejores prácticas para entrenar un modelo de aprendizaje automático con un conjunto de datos pequeño?"
        )
        print("Respuesta de Gemini API:")
        print(respuesta.text)
    except Exception as e:
        print(f"Error al ejecutar consulta a Gemini API: {e}")  

if __name__ == "__main__":
    ejecutar_consulta() 