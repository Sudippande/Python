import os
import shutil
from datetime import datetime

def auto_backup(extension=".py"):
    # 1. Create a timestamped folder name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = f"backup_{timestamp}"

    # 2. Create the backup folder
    os.makedirs(backup_folder, exist_ok=True)

    # 3. Scan current folder for files with the given extension
    files_backed_up = 0
    for file in os.listdir():
        if file.endswith(extension) and os.path.isfile(file):
            shutil.copy(file, os.path.join(backup_folder, file))
            files_backed_up += 1

    # 4. Summary
    if files_backed_up:
        print(f"✅ {files_backed_up} '{extension}' files backed up in folder '{backup_folder}'")
    else:
        print(f"⚠️ No '{extension}' files found to back up.")

# Run the backup
auto_backup(".py")
