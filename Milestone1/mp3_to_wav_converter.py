import os
from pydub import AudioSegment

def convert_mp3_to_wav(input_folder, output_folder):
    """
    Converts all MP3 files in the input folder to WAV format and saves them in the output folder.

    :param input_folder: Path to the folder containing MP3 files.
    :param output_folder: Path to the folder where WAV files will be saved.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each MP3 file in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".wav"):
            mp3_path = os.path.join(input_folder, file_name)
            wav_file_name = os.path.splitext(file_name)[0] + ".wav"
            wav_path = os.path.join(output_folder, wav_file_name)

            try:
                # Convert MP3 to WAV
                print(f"Converting {file_name} to {wav_file_name}...")
                audio = AudioSegment.from_mp3(mp3_path)
                audio.export(wav_path, format="wav")
                print(f"Saved: {wav_path}")
            except Exception as e:
                print(f"Failed to convert {file_name}: {e}")

if __name__ == "__main__":
    input_folder = input("Enter the path to the folder with MP3 files: ").strip()
    output_folder = input("Enter the path to the output folder for WAV files: ").strip()

    convert_mp3_to_wav(input_folder, output_folder)
    print("Conversion complete.")
