from gtts import gTTS
from pydub import AudioSegment
import os

# Ensure ffmpeg is installed for pydub to work
# Use website to learn to change language or accent
# https://gtts.readthedocs.io/en/latest/module.html#localized-accents

# Phrase (change this to have tts say whatever)
phrase = "Hey Jarvis"

# Output folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
output_folder = os.path.join(downloads_folder, "hey_jarvis_folder1")
os.makedirs(output_folder, exist_ok=True)

# Generate 100 files
for i in range(1, 101):
    # Temporary file path for the mp3
    temp_mp3_path = os.path.join(output_folder, f"temp_ng_hey_jarvis_{i}.mp3")

    # Final file path for the wav
    wav_file_path = os.path.join(output_folder, f"ng_hey_jarvis_{i}.wav")

    # Create TTS and save as mp3
    tts = gTTS(phrase, lang='en', tld='com.ng')  # change language/accent
    tts.save(temp_mp3_path)

    # Convert mp3 to wav using pydub
    audio = AudioSegment.from_mp3(temp_mp3_path)
    audio.export(wav_file_path, format="wav")
    print(f"Generated {wav_file_path}")

    # Remove temporary mp3 file
    os.remove(temp_mp3_path)
