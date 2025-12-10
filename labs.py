from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
import os

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

# This returns a generator/iterator
audio_stream = elevenlabs.text_to_speech.convert(
    text="The first move is what sets everything in motion.",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

output_filename = "motion_quote.mp3"

try:
    print(f"Writing audio stream to '{output_filename}'...")
    with open(output_filename, "wb") as f:
        # Iterate over the stream chunks and write each one
        for chunk in audio_stream:
            if chunk:
                f.write(chunk)
    
    print(f"\nSuccess! Audio saved to '{output_filename}'")
    print("Please download this file from your GitHub file explorer to listen to it locally.")

except IOError as e:
    print(f"\nError saving file: {e}")

