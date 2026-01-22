import os
import shutil

def copy_files(src_dir, dst_dir, extension=None):
    """Copy files from src to dst, excluding 'nul' and hidden files."""
    os.makedirs(dst_dir, exist_ok=True)

    for item in os.listdir(src_dir):
        if item == 'nul' or item.startswith('.'):
            continue

        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dst_dir, item)

        if os.path.isdir(src_path):
            copy_dir_recursive(src_path, dst_path)
        elif extension is None or item.endswith(extension):
            try:
                with open(src_path, 'rb') as f:
                    content = f.read()
                with open(dst_path, 'wb') as f:
                    f.write(content)
                print(f"Copied: {item}")
            except Exception as e:
                print(f"Error: {item} - {e}")

def copy_dir_recursive(src, dst):
    """Recursively copy directory, excluding nul files."""
    os.makedirs(dst, exist_ok=True)

    for item in os.listdir(src):
        if item == 'nul' or item.startswith('.'):
            continue

        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isdir(src_path):
            copy_dir_recursive(src_path, dst_path)
        else:
            try:
                with open(src_path, 'rb') as f:
                    content = f.read()
                with open(dst_path, 'wb') as f:
                    f.write(content)
            except Exception as e:
                print(f"Error: {src_path} - {e}")

# Copy pages
print("Copying pages...")
os.makedirs(r'F:\cbec_fresh\pages', exist_ok=True)
copy_files(r'F:\thecbec.org\pages', r'F:\cbec_fresh\pages', '.md')

# Copy wp-content (media)
print("\nCopying media files...")
copy_dir_recursive(r'F:\thecbec.org\wp-content', r'F:\cbec_fresh\wp-content')

print("\nDone!")
