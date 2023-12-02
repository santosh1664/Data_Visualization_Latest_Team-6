import os
import platform

def get_downloads_folder():
    """
    Get the path to the user's Downloads folder.

    Returns:
    str: Path to the Downloads folder.
    """
    home = os.path.expanduser("~")
    os_type = platform.system()

    if os_type == 'Windows':
        downloads_path = os.path.join(home, 'Downloads')
    elif os_type == 'Darwin':
        downloads_path = os.path.join(home, 'Downloads')
    elif os_type == 'Linux':
        xdg = os.path.join(home, '.config/user-dirs.dirs')
        if os.path.exists(xdg):
            with open(xdg, 'r') as file:
                for line in file:
                    if line.startswith('XDG_DOWNLOAD_DIR'):
                        path = line.split('"')[1]
                        downloads_path = os.path.join(home, os.path.basename(path).strip())
                        break
                else:
                    downloads_path = os.path.join(home, 'Downloads')
        else:
            downloads_path = os.path.join(home, 'Downloads')
    else:
        return None  # Or some default path

    if os.path.exists(downloads_path) and os.path.isdir(downloads_path):
        return downloads_path
    else:
        return None  # Downloads folder does not exist or is not a directory

# Example usage
downloads_folder = get_downloads_folder()
if downloads_folder:
    print(f"Downloads folder: {downloads_folder}")
else:
    print("Could not determine the Downloads folder or it does not exist.")
