from gtts import gTTS
import os

# use website to learn to change language or accent
# https://gtts.readthedocs.io/en/latest/module.html#localized-accents

# phrase (change this to have tts say whatever)
phrase = "Hey Jarvis"

# Output folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
output_folder = os.path.join(downloads_folder, "hey_jarvis_folder1")
os.makedirs(output_folder, exist_ok=True)

# Generate 100 files
for i in range(1, 101):
    tts = gTTS(phrase, lang='en', tld='com.ng') # change language/accent
    file_path = os.path.join(output_folder, f"ng_hey_jarvis_{i}.wav")
    tts.save(file_path)
    print(f"Generated {file_path}")