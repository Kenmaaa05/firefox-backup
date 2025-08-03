import os
import zipfile
from datetime import datetime, timedelta

SOURCE_DIR = r"PATH TO FIREFOX\PROFILES"
BACKUP_DIR = r"PATH TO BACKUP FOLDER"
backup_days = 14

os.makedirs(BACKUP_DIR, exist_ok=True)

# deleting older than 14 days zip files
cutoff_time = datetime.now() - timedelta(days=backup_days)

for file in os.listdir(BACKUP_DIR):
    file_path = os.path.join(BACKUP_DIR, file)
    if file.endswith(".zip") and os.path.isfile(file_path):
        file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
        if file_mtime < cutoff_time:
            try:
                os.remove(file_path)
                print(f"Deleted old backup: {file}")
            except Exception as e:
                print(f"Failed to delete {file}: {e}")

# creating new backup
timestamp = datetime.now().strftime("%Y-%m-%d__%H-%M-%S")
backup_name = f"firefox_profiles_backup_{timestamp}.zip"
backup_path = os.path.join(BACKUP_DIR, backup_name)

with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            abs_file_path = os.path.join(root, file)
            arcname = os.path.relpath(abs_file_path, SOURCE_DIR)
            zipf.write(abs_file_path, arcname)

print(f"Backup created successfully at: {backup_path}")
