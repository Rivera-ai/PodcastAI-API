import requests
from pathlib import Path
import json
from typing import Optional, Dict, Union, List
from pprint import pprint

class PodcastGeneratorClient:
    """Cliente para interactuar con la API del generador de podcasts"""
    
    def __init__(self, api_key: str, base_url: str = "https://www.podcastai.tech"):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.headers = {"X-Api-Key": api_key}
        
    def check_health(self) -> Dict:
        """Verifica el estado de la API"""
        response = requests.get(
            f"{self.base_url}/api/v1/health",
            headers=self.headers
        )
        return response.json()
    
    def list_voices(self) -> List[Dict]:
        """Lista todas las voces disponibles"""
        response = requests.get(
            f"{self.base_url}/api/v1/voices",
            headers=self.headers
        )
        if response.status_code != 200:
            raise Exception(f"Error al listar voces: {response.json()['error']}")
        return response.json()
    
    def upload_voice(self, voice_file_path: Union[str, Path], voice_name: str, voice_type: str) -> Dict:
        """
        Sube una nueva voz personalizada
        
        Args:
            voice_file_path: Ruta al archivo de voz (.wav)
            voice_name: Nombre para identificar la voz
            voice_type: Tipo de voz ('sara' o 'robert')
            
        Returns:
            Dict con la información de la voz subida
        """
        files = {
            'voice_file': ('voice.wav', open(voice_file_path, 'rb'), 'audio/wav')
        }
        data = {
            'voice_name': voice_name,
            'voice_type': voice_type
        }
        response = requests.post(
            f"{self.base_url}/api/v1/voices",
            headers=self.headers,
            files=files,
            data=data
        )
        if response.status_code != 200:
            raise Exception(f"Error al subir voz: {response.json()['error']}")
        return response.json()
    
    def delete_voice(self, voice_id: int) -> Dict:
        """
        Elimina una voz personalizada
        
        Args:
            voice_id: ID de la voz a eliminar
            
        Returns:
            Dict con la confirmación de eliminación
        """
        response = requests.delete(
            f"{self.base_url}/api/v1/voices/{voice_id}",
            headers=self.headers
        )
        if response.status_code != 200:
            raise Exception(f"Error al eliminar voz: {response.json()['error']}")
        return response.json()
    
    def generate_podcast_from_pdf(
        self,
        pdf_path: Union[str, Path],
        language: str = "es",
        podcast_length: str = "Base (3-5 min)",
        question: Optional[str] = None,
        use_custom_voices: bool = False,
        custom_voice_sara: Optional[str] = None,
        custom_voice_robert: Optional[str] = None
    ) -> Dict:
        """
        Genera un podcast a partir de un archivo PDF
        
        Args:
            pdf_path: Ruta al archivo PDF
            language: Idioma del podcast ('es', 'en', etc)
            podcast_length: "Base (3-5 min)" o "Extended (8-10 min)"
            question: Pregunta o enfoque específico (opcional)
            use_custom_voices: Si se usarán voces personalizadas
            custom_voice_sara: URL de Cloudinary para voz de Sara
            custom_voice_robert: URL de Cloudinary para voz de Robert
            
        Returns:
            Dict con la URL del podcast y la transcripción
        """
        files = {'file': open(pdf_path, 'rb')}
        data = {
            'language': language,
            'podcast_length': podcast_length,
            'use_custom_voices': str(use_custom_voices).lower()
        }
        
        if question:
            data['question'] = question
            
        if use_custom_voices:
            if not (custom_voice_sara and custom_voice_robert):
                raise ValueError("Se requieren URLs para ambas voces personalizadas")
            data['custom_voice_sara'] = custom_voice_sara
            data['custom_voice_robert'] = custom_voice_robert
            
        response = requests.post(
            f"{self.base_url}/api/v1/generate-podcast",
            headers=self.headers,
            files=files,
            data=data
        )
        
        if response.status_code != 200:
            raise Exception(f"Error en la API: {response.json()['error']}")
            
        return response.json()
    
    def generate_podcast_from_url(
        self,
        url: str,
        language: str = "es",
        podcast_length: str = "Base (3-5 min)",
        question: Optional[str] = None,
        use_custom_voices: bool = False,
        custom_voice_sara: Optional[str] = None,
        custom_voice_robert: Optional[str] = None
    ) -> Dict:
        """
        Genera un podcast a partir de una URL
        
        Args:
            url: URL del contenido a procesar
            language: Idioma del podcast ('es', 'en', etc)
            podcast_length: "Base (3-5 min)" o "Extended (8-10 min)"
            question: Pregunta o enfoque específico (opcional)
            use_custom_voices: Si se usarán voces personalizadas
            custom_voice_sara: URL de Cloudinary para voz de Sara
            custom_voice_robert: URL de Cloudinary para voz de Robert
            
        Returns:
            Dict con la URL del podcast y la transcripción
        """
        data = {
            'url': url,
            'language': language,
            'podcast_length': podcast_length,
            'use_custom_voices': str(use_custom_voices).lower()
        }
        
        if question:
            data['question'] = question
            
        if use_custom_voices:
            if not (custom_voice_sara and custom_voice_robert):
                raise ValueError("Se requieren URLs para ambas voces personalizadas")
            data['custom_voice_sara'] = custom_voice_sara
            data['custom_voice_robert'] = custom_voice_robert
            
        response = requests.post(
            f"{self.base_url}/api/v1/generate-podcast",
            headers=self.headers,
            data=data
        )
        
        if response.status_code != 200:
            raise Exception(f"Error en la API: {response.json()['error']}")
            
        return response.json()

def main():
    """Ejemplo de uso del cliente"""
    # Crear instancia del cliente con API key
    API_KEY = "pk_YOUR_API_KEY"
    client = PodcastGeneratorClient(api_key=API_KEY)
    
    # Verificar estado de la API
    print("Verificando estado de la API...")
    health = client.check_health()
    pprint(health)
    
    # Listar voces disponibles
    print("\nListando voces disponibles...")
    voices = client.list_voices()
    pprint(voices)
    
    # Subir una nueva voz
    print("\nSubiendo nueva voz...")
    try:
        result = client.upload_voice(
            voice_file_path="Voice/male.wav",
            voice_name="TestAPI",
            voice_type="sara"
        )
        pprint(result)
    except Exception as e:
        print(f"Error al subir voz: {str(e)}")
    
    # Eliminar una voz
    print("\nEliminando voz...")
    try:
        result = client.delete_voice(voice_id=6)
        pprint(result)
    except Exception as e:
        print(f"Error al eliminar voz: {str(e)}")
    
    # Ejemplo de generación de podcast desde URL
    print("\nGenerando podcast desde URL...")
    try:
        result = client.generate_podcast_from_url(
            url="https://arxiv.org/pdf/2410.01131",
            language="es",
            podcast_length="Extended (8-10 min)",
            question="Explica esto de manera simple"
        )
        print("\nURL del podcast:", result['podcast_url'])
        print("\nTranscripción:")
        for line in result['transcript']:
            print(f"{line['speaker']}: {line['text']}")
    except Exception as e:
        print(f"Error al generar podcast desde URL: {str(e)}")

if __name__ == "__main__":
    main()