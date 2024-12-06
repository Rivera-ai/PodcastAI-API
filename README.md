# PodcastAI API Client

A Python client that provides a simple interface to interact with the PodcastAI API, allowing you to generate podcasts from PDFs or URLs and manage custom voices.

## Web Documentation

If you need to see some options or new features that we haven't covered yet in the API client you can check it out here: https://www.podcastai.tech/api/docs

## Installation

```bash
pip install requests
```

## Setup

To use the client, you'll need a valid PodcastAI API key. Initialize the client like this:

```python
from podcast_generator import PodcastGeneratorClient

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

### 3. Podcast Generation

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

#### `generate_podcast_from_pdf(...) -> Dict`
- Generates a podcast from a PDF file
- Main parameters:
  - `pdf_path`: Path to PDF file
  - `language`: Podcast language ('en', 'es', etc)
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

## Error Handling

The client includes error handling for main operations. Errors are raised as exceptions with descriptive messages:

```python
try:
    result = client.generate_podcast_from_url(...)
except Exception as e:
    print(f"Error: {str(e)}")
```

## Complete Example

```python
from podcast_generator import PodcastGeneratorClient

# Initialize client
API_KEY = "your_api_key_here"
client = PodcastGeneratorClient(api_key=API_KEY)

# Check status
health = client.check_health()
print("API Status:", health)

# Generate podcast
try:
    result = client.generate_podcast_from_url(
        url="https://example.com/article",
        language="en",
        podcast_length="Base (3-5 min)",
        question="Main summary"
    )
    print("Podcast URL:", result['podcast_url'])
    print("\nTranscript:")
    for line in result['transcript']:
        print(f"{line['speaker']}: {line['text']}")
except Exception as e:
    print(f"Error generating podcast: {str(e)}")
```

## Important Notes

1. Voice files must be in WAV format
2. Custom voices require Cloudinary URLs
3. API key should be kept secure and not shared
4. Podcasts can be generated in multiple languages
5. Two podcast lengths are available: Base (3-5 min) and Extended (8-10 min)

## Common Use Cases

### Educational Content
```python
result = client.generate_podcast_from_pdf(
    pdf_path="lecture_notes.pdf",
    language="en",
    podcast_length="Extended (8-10 min)",
    question="Explain the key concepts in simple terms"
)
```

### News Summaries
```python
result = client.generate_podcast_from_url(
    url="https://example.com/news-article",
    language="en",
    podcast_length="Base (3-5 min)",
    question="What are the main events and their implications?"
)
```

## Supported Languages

The API supports multiple languages including:
- English (en)
- Spanish (es)
- Additional languages may be available (check API documentation)

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
