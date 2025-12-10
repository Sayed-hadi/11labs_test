from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
# Removed 'from elevenlabs.play import play'
import os

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = elevenlabs.text_to_speech.convert(
    text="The first move is what sets everything in motion.",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

# --- MODIFIED SECTION ---
output_filename = "motion_quote.mp3"

try:
    # Write the received audio bytes to a file
    with open(output_filename, "wb") as f:
        f.write(audio)
    
    print(f"\nSuccess! Audio saved to '{output_filename}'")
    print("Please download this file from your GitHub file explorer to listen to it locally.")

except IOError as e:
    print(f"\nError saving file: {e}")

# The 'play(audio)' line is gone.
