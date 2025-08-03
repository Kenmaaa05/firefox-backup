@echo off
echo Starting Firefox profile backup and upload...

cd /d "PATH TO BACKUP FOLDER"

echo Running backup script...
python backup_script.py

echo Uploading to Google Drive...
python upload_to_drive.py

echo Backup and upload complete.
pause
