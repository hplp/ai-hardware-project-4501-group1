import os
import shutil
import string


def combine_and_rename_files(input_base_folder, output_folder):
    """
    Combines files from subfolders into a single folder and renames them
    with a letter corresponding to the subfolder.

    :param input_base_folder: Path to the base folder containing subfolders.
    :param output_folder: Path to the folder where combined files will be stored.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Get all subfolders in the input base folder
    subfolders = [f for f in os.listdir(input_base_folder) if os.path.isdir(os.path.join(input_base_folder, f))]

    # Sort subfolders alphabetically for consistent letter assignment
    subfolders.sort()

    # Assign a letter to each folder (e.g., a, b, c...)
    folder_letter_mapping = {subfolders[i]: string.ascii_lowercase[i] for i in range(len(subfolders))}

    print(f"Folder to letter mapping: {folder_letter_mapping}")

    # Iterate through each folder
    for folder_name in subfolders:
        folder_path = os.path.join(input_base_folder, folder_name)
        folder_letter = folder_letter_mapping[folder_name]

        # Process each file in the folder
        for file_name in os.listdir(folder_path):
            # Build full file paths
            source_path = os.path.join(folder_path, file_name)

            # Skip if not a file
            if not os.path.isfile(source_path):
                continue

            # Rename the file by adding the folder's letter
            new_file_name = f"{os.path.splitext(file_name)[0]}{folder_letter}{os.path.splitext(file_name)[1]}"
            destination_path = os.path.join(output_folder, new_file_name)

            # Copy the file to the output folder
            shutil.copy(source_path, destination_path)
            print(f"Copied and renamed: {source_path} -> {destination_path}")


if __name__ == "__main__":
    # Path to the folder containing all subfolders
    input_base_folder = os.path.expanduser("~/Downloads/turn_off_lights_folder")

    # Path to the main output folder
    output_folder = os.path.expanduser("~/Downloads/off_consolidated_files")

    combine_and_rename_files(input_base_folder, output_folder)
    print("All files combined and renamed successfully.")
