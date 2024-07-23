import os
import shutil
import sys

def create_folders_with_template(n):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(base_dir, '..', 'templates')
    template_script = os.path.join(templates_dir, 'main.py')

    if not os.path.exists(template_script):
        print(f"Template script not found at {template_script}")
        return

    for i in range(1, n + 1):
        folder_name = f"problem_{i}"
        folder_path = os.path.join(base_dir, '..', folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        destination_script = os.path.join(folder_path, 'main.py')
        shutil.copy(template_script, destination_script)
        print(f"Created {folder_path} with template script.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_folders.py <number_of_folders>")
    else:
        try:
            n = int(sys.argv[1])
            if n > 0:
                create_folders_with_template(n)
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")
