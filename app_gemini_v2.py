import os
from google import genai
from dotenv import load_dotenv
from google.genai import types
 
# Carga de variables de entorno desde el archivo .env
load_dotenv()
 
clave_api = os.getenv("GEMINI_API_KEY")
 
# Inicializa el cliente de Gemini con la clave API
cliente = genai.Client(api_key=clave_api)
 
def ejecutar_consulta():
    print("⛷️ Ejecutando consulta a Gemini...")
 
    texto = """
           Redacta una descripción atractiva del producto UPTC FIT, el cual es un reloj inteligente diseñado para estudiantes universitarios,
            que ofrece funciones de seguimiento de actividad física, notificaciones inteligentes y una interfaz intuitiva para ayudar a
            los estudiantes a mantenerse organizados y saludables durante su vida académica.
    """
 
    #prompt = f""" Resume la conversación entre el cliente y el agente de servicio al cliente, en 4 puntos claves y al final indicar si se resolvió el problema del cliente o no. La conversación es la siguiente: {texto}"""
 
 
    configuracion = types.GenerateContentConfig(
        temperature=1.0,
        max_output_tokens=5000)
 
    try:
        respuesta = cliente.models.generate_content(
            model="gemini-3.5-flash",
            contents=texto,
            config=configuracion
        )
        print("Respuesta de Gemini:")
        print(respuesta.text)
 
        print("=="*30)
        print("tokens usados:", respuesta.usage_metadata.candidates_token_count)
        print(f"Precio estimado de la respuesta: {respuesta.usage_metadata.candidates_token_count * (1.5/1000000)} USD")
 
    except Exception as e:
        print("Error al ejecutar la consulta:", e)
if __name__ == "__main__":
    ejecutar_consulta()
 