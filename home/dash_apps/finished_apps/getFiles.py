import os

import pyttsx3

from home.dash_apps.finished_apps.getDownloadFolder import get_downloads_folder

def list_filenames_in_directory(directory_path):

    try:
        all_files = os.listdir(directory_path)

        # Filter for Excel and CSV files
        excel_csv_files = [f for f in all_files if f.endswith('.xlsx') or f.endswith('.xls') or f.endswith('.csv')]
        numbered_files = [f"{index + 1}. {filename}" for index, filename in enumerate(excel_csv_files)]
        return excel_csv_files, numbered_files

    except FileNotFoundError:
        print("Directory not found.")
        return []
def read_filenames_aloud(filenames):
    """
    Reads the list of filenames aloud using speech synthesis.

    Args:
    filenames (list): A list of filenames to be read.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    for filename in filenames:
        engine.say(filename)
        engine.runAndWait()

# Example usage
downloads_folder_path = get_downloads_folder()
filenames, numbered_files = list_filenames_in_directory(downloads_folder_path)
read_filenames_aloud(numbered_files)
print(numbered_files)
