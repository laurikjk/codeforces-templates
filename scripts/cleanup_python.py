import os
import shutil
import sys

def cleanup_folders(n):
    base_dir = os.path.dirname(os.path.abspath(__file__))

    for i in range(1, n + 1):
        folder_name = f"problem_{i}"
        folder_path = os.path.join(base_dir, '..', folder_name)

        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
            print(f"Deleted {folder_path}")
        else:
            print(f"Folder {folder_path} does not exist or is not a directory.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cleanup_folders.py <number_of_folders>")
    else:
        try:
            n = int(sys.argv[1])
            if n > 0:
                cleanup_folders(n)
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")
