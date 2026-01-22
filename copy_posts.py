import os
import shutil

src_dir = r'F:\thecbec.org\_posts'
dst_dir = r'F:\cbec_fresh\_posts'

# Get list of md files (excluding 'nul' and other weird names)
for filename in os.listdir(src_dir):
    if filename.endswith('.md') and filename != 'nul' and not filename.startswith('.'):
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(dst_dir, filename)

        # Read content and write to destination
        try:
            with open(src_path, 'r', encoding='utf-8') as f:
                content = f.read()
            with open(dst_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Copied: {filename}")
        except Exception as e:
            print(f"Error copying {filename}: {e}")

print("Done!")
