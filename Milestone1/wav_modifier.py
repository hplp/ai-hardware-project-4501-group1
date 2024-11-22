import os
import random
from pydub import AudioSegment

def modify_wav_files(input_folder, output_folder):
    """
    Slightly modifies all .wav files in the input folder to ensure they have unique hashes.
    Modifications include random volume adjustments and adding a small silence.

    :param input_folder: Path to the folder containing the original .wav files.
    :param output_folder: Path to the folder where modified .wav files will be saved.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".wav"):
            file_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)

            try:
                # Load the audio file
                audio = AudioSegment.from_wav(file_path)

                # Modify the audio slightly
                random_volume_adjustment = random.uniform(-0.05, 0.05)  # Random adjustment between -0.05 and +0.05 dB
                modified_audio = (
                    AudioSegment.silent(duration=50) +  # Add 50ms silence at the start
                    audio +  # Original audio
                    AudioSegment.silent(duration=50)  # Add 50ms silence at the end
                )

                # Apply the random volume adjustment
                modified_audio = modified_audio + random_volume_adjustment

                # Export the modified audio
                modified_audio.export(output_path, format="wav")
                print(f"Modified and saved: {output_path}")

            except Exception as e:
                print(f"Failed to process {file_name}: {e}")

if __name__ == "__main__":
    # Input folder containing original .wav files
    input_folder = input("Enter the path to the folder with original .wav files: ").strip()

    # Output folder to save modified .wav files
    output_folder = input("Enter the path to the folder for modified .wav files: ").strip()

    modify_wav_files(input_folder, output_folder)
    print("All files processed and saved to the output folder.")
