# PodcastAI API Client

A Python client that provides a simple interface to interact with the PodcastAI API, allowing you to generate podcasts from PDFs or URLs, manage custom voices, and convert text to speech.

## Web Documentation

If you need to see some options or new features that we haven't covered yet in the API client you can check it out here: https://www.podcastai.tech/api/docs

## Installation

```bash
git clone https://github.com/Rivera-ai/PodcastAI-API
cd PodcastAI-API
pip install -e .
```

## Setup

To use the client, you'll need a valid PodcastAI API key. Initialize the client like this:

```python
from podcastai import PodcastGeneratorClient

client = PodcastGeneratorClient(api_key="your_api_key_here")
```

## Main Features

### 1. Check API Health

```python
health = client.check_health()
print(health)
```

### 2. Voice Management

#### List Available Voices
```python
voices = client.list_voices()
print(voices)
```

#### Upload New Voice
```python
result = client.upload_voice(
    voice_file_path="path/to/your/file.wav",
    voice_name="VoiceName",
    voice_type="sara"  # or "robert"
)
```

#### Delete Voice
```python
result = client.delete_voice(voice_id=1)
```

### 3. Text to Speech (TTS)

Convert text to speech using different voices and languages:

```python
result = client.TTS(
    text="Hello, this is a test message",
    language="en",
    speaker="Sara",  # or "Robert"
    use_custom_voice=False,
    custom_voice=None  # Cloudinary URL for custom voice if use_custom_voice=True
)

print("Audio URL:", result['audio_url'])
```

### 4. Podcast Generation

#### From PDF
```python
result = client.generate_podcast_from_pdf(
    pdf_path="document.pdf",
    language="en",
    podcast_length="Base (3-5 min)",
    question="What are the main points?",
    use_custom_voices=False
)

print("Podcast URL:", result['podcast_url'])
print("\nTranscript:")
for line in result['transcript']:
    print(f"{line['speaker']}: {line['text']}")
```

#### From URL
```python
result = client.generate_podcast_from_url(
    url="https://example.com/article",
    language="en",
    podcast_length="Extended (8-10 min)",
    question="Explain this in simple terms",
    use_custom_voices=True,
    custom_voice_sara="sara_voice_url",
    custom_voice_robert="robert_voice_url"
)
```

## Method Reference

### PodcastGeneratorClient

#### `__init__(api_key: str, base_url: str = "https://www.podcastai.tech")`
- Initializes the client with API key and base URL
- Parameters:
  - `api_key`: API key for authentication
  - `base_url`: API base URL (optional)

#### `check_health() -> Dict`
- Checks API health status
- Returns: Dictionary with API status

#### `list_voices() -> List[Dict]`
- Lists all available voices
- Returns: List of dictionaries containing voice information

#### `upload_voice(voice_file_path: Union[str, Path], voice_name: str, voice_type: str) -> Dict`
- Uploads a new custom voice
- Parameters:
  - `voice_file_path`: Path to voice file (.wav)
  - `voice_name`: Name to identify the voice
  - `voice_type`: Voice type ('sara' or 'robert')
- Returns: Dictionary with uploaded voice information

#### `delete_voice(voice_id: int) -> Dict`
- Deletes a custom voice
- Parameters:
  - `voice_id`: ID of the voice to delete
- Returns: Dictionary with deletion confirmation

#### `TTS(text: str, language: str = "es", speaker: str = "Sara", use_custom_voice: bool = False, custom_voice: Optional[str] = None) -> Dict`
- Converts text to speech
- Parameters:
  - `text`: Text to convert to speech
  - `language`: Text language (see Supported Languages)
  - `speaker`: Voice to use ('Sara' or 'Robert')
  - `use_custom_voice`: Whether to use a custom voice
  - `custom_voice`: Cloudinary URL for custom voice (required if use_custom_voice=True)
- Returns: Dictionary with audio URL and metadata

#### `generate_podcast_from_pdf(...) -> Dict`
- Generates a podcast from a PDF file
- Main parameters:
  - `pdf_path`: Path to PDF file
  - `language`: Podcast language (see Supported Languages)
  - `podcast_length`: "Base (3-5 min)" or "Extended (8-10 min)"
  - `question`: Specific question or focus (optional)
  - `use_custom_voices`: Whether to use custom voices
  - `custom_voice_sara`: Cloudinary URL for Sara's voice (optional)
  - `custom_voice_robert`: Cloudinary URL for Robert's voice (optional)
- Returns: Dictionary with podcast URL and transcript

#### `generate_podcast_from_url(...) -> Dict`
- Generates a podcast from a URL
- Parameters: Similar to `generate_podcast_from_pdf`, but with `url` instead of `pdf_path`
- Returns: Dictionary with podcast URL and transcript

## Supported Languages

The API supports the following languages:
- English (en)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)
- Portuguese (pt)
- Polish (pl)
- Turkish (tr)
- Russian (ru)
- Dutch (nl)
- Czech (cs)
- Arabic (ar)
- Chinese (zh)
- Hungarian (hu)
- Korean (ko)
- Hindi (hi)

## Error Handling

The client includes error handling for main operations. Errors are raised as exceptions with descriptive messages:

```python
try:
    result = client.TTS(text="Hello world", language="en")
except Exception as e:
    print(f"Error: {str(e)}")
```

## Complete Example

```python
from podcastai import PodcastGeneratorClient

# Initialize client
API_KEY = "your_api_key_here"
client = PodcastGeneratorClient(api_key=API_KEY)

# Check status
health = client.check_health()
print("API Status:", health)

# Generate TTS
try:
    result = client.TTS(
        text="Welcome to PodcastAI",
        language="en",
        speaker="Sara"
    )
    print("Audio URL:", result['audio_url'])
except Exception as e:
    print(f"Error generating audio: {str(e)}")

# Generate podcast
try:
    result = client.generate_podcast_from_url(
        url="https://example.com/article",
        language="en",
        podcast_length="Base (3-5 min)",
        question="Main summary"
    )
    print("Podcast URL:", result['podcast_url'])
except Exception as e:
    print(f"Error generating podcast: {str(e)}")
```

## Important Notes

1. Voice files must be in WAV format
2. Custom voices require Cloudinary URLs
3. API key should be kept secure and not shared
4. Both TTS and podcasts support multiple languages
5. Two podcast lengths available: Base (3-5 min) and Extended (8-10 min)

## Support

For additional support or to report issues:
1. Check the API documentation
2. Contact the PodcastAI support team
3. Visit the official website for updates

## Contributing

If you'd like to contribute to this client:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request