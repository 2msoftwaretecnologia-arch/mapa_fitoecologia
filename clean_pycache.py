import os
import shutil

def delete_pycache(base_directory):
    total_deleted = 0
    for root, dirs, files in os.walk(base_directory):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                full_path = os.path.join(root, dir_name)
                try:
                    shutil.rmtree(full_path)
                    print(f"Deleted: {full_path}")
                    total_deleted += 1
                except Exception as e:
                    print(f"Error deleting {full_path}: {e}")
    print(f"\nTotal '__pycache__' folders deleted: {total_deleted}")

# Example usage
directory = r"C:\\Users\\V1CT0R\\Downloads\\softwares\\envimap\\mapa_fitoecologia\\"
delete_pycache(directory)
