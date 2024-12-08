from podcastai import PodcastGeneratorClient
import time

def test_tts_client():
    """Prueba las funcionalidades del cliente TTS"""
    
    # Configuración
    API_KEY = "pk_YOUR_API_KEY"  # Reemplaza con tu API key
    
    # Inicializar cliente
    client = PodcastGeneratorClient(api_key=API_KEY)
    
    # Lista de pruebas
    tests = [
        {
            "name": "Test básico con voz Sara",
            "params": {
                "text": "Hola, esta es una prueba básica con la voz de Sara.",
                "language": "es",
                "speaker": "Sara",
                "use_custom_voice": False
            }
        },
        {
            "name": "Test básico con voz Robert",
            "params": {
                "text": "Hola, esta es una prueba básica con la voz de Robert.",
                "language": "es",
                "speaker": "Robert",
                "use_custom_voice": False
            }
        },
        {
            "name": "Test con voz personalizada para Sara",
            "params": {
                "text": "Esta es una prueba con voz personalizada para Sara.",
                "language": "es",
                "speaker": "Sara",
                "use_custom_voice": True,
                "custom_voice": "https://res.cloudinary.com/dmtomxyvm/video/upload/v1731889883/voices/exdawrxdkcgonrxcc2ij.wav"
            }
        },
        {
            "name": "Test con voz personalizada para Robert",
            "params": {
                "text": "Esta es una prueba con voz personalizada para Robert.",
                "language": "es",
                "speaker": "Robert",
                "use_custom_voice": True,
                "custom_voice": "https://res.cloudinary.com/dmtomxyvm/video/upload/v1731889883/voices/exdawrxdkcgonrxcc2ij.wav"
            }
        }
    ]

    # Ejecutar pruebas
    for test in tests:
        print(f"\nEjecutando: {test['name']}")
        print("-" * 50)
        
        try:
            # Hacer la petición
            print("Parámetros de la prueba:")
            for key, value in test['params'].items():
                print(f"  {key}: {value}")
            
            response = client.TTS(**test['params'])
            
            # Imprimir resultado
            print("\nRespuesta:")
            print(f"  Audio URL: {response.get('audio_url', 'No disponible')}")
            print(f"  Audio ID: {response.get('audio_id', 'No disponible')}")
            print(f"  Metadata: {response.get('metadata', {})}")
            
            # Esperar entre pruebas para no sobrecargar el servidor
            time.sleep(5)
            
        except Exception as e:
            print(f"Error: {str(e)}")
        
        print("-" * 50)

def main():
    """Función principal"""
    try:
        test_tts_client()
    except KeyboardInterrupt:
        print("\nPruebas interrumpidas por el usuario")
    except Exception as e:
        print(f"\nError inesperado: {str(e)}")

if __name__ == "__main__":
    main()