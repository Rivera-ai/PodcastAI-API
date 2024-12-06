from podcastai import PodcastGeneratorClient

def main():
    """Ejemplo de uso del cliente"""
    # Crear instancia del cliente con API key
    API_KEY = "pk_YOUR_API_KEY"
    client = PodcastGeneratorClient(api_key=API_KEY)
    
    # Verificar estado de la API
    print("Verificando estado de la API...")
    health = client.check_health()
    print(health)
    
    # Listar voces disponibles
#    print("\nListando voces disponibles...")
#    voices = client.list_voices()
#    print(voices)
    
    # Subir una nueva voz
#    print("\nSubiendo nueva voz...")
#    try:
#        result = client.upload_voice(
#            voice_file_path="Voice/male.wav",
#            voice_name="TestAPI",
#            voice_type="sara"
#        )
#        print(result)
#    except Exception as e:
#        print(f"Error al subir voz: {str(e)}")
    
    # Eliminar una voz
#    print("\nEliminando voz...")
#    try:
#        result = client.delete_voice(voice_id=6)
#        print(result)
#    except Exception as e:
#        print(f"Error al eliminar voz: {str(e)}")
    
    # Ejemplo de generación de podcast desde URL
#    print("\nGenerando podcast desde URL...")
#    try:
#        result = client.generate_podcast_from_url(
#            url="https://arxiv.org/pdf/2410.01131",
#            language="es",
#            podcast_length="Extended (8-10 min)",
#            question="Explica esto de manera simple"
#        )
#        print("\nURL del podcast:", result['podcast_url'])
#        print("\nTranscripción:")
#        for line in result['transcript']:
#            print(f"{line['speaker']}: {line['text']}")
#    except Exception as e:
#        print(f"Error al generar podcast desde URL: {str(e)}")

if __name__ == "__main__":
    main()