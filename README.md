# Firefox Profile Backup (local and google drive)

Brave crashed and I lost a few of my profiles so I decided to switch to firefox and make sure my profiles and the broswer data inside is safe and secured.

The scripts will do 2 things:

**1. `backup_script.py`**

- zip the multiple profiles.
- save them in a backup folder of your choice.
- delete the zip files that are older than 14 days.

**2. `upload_to_drive.py`**

- upload the latest zip file to your google drive. 
- make sure that you have a folder created in the google drive to save the zip files.
- I'll add the function to delete the zip files older than 2 weeks later. 

Simply double click and run the bat file and it'll be done.

---

> ⚠️ You need to have the google drive API key. so make sure you have that configured. You will need credentials.token and token.json for authentication and uploading.

### 1. Here's how to setup the api

1. Go to Google Cloud Console<br>
2. Create a new project<br>
3. Enable the Google Drive API<br>
4. Configure an OAuth 2.0 Client ID (Desktop app)<br>
5. Download the `credentials.json` and place it in the project folder (keep it private!)<br> you'll get the `token.json` after authentication
6. Add your Google account as a test user under OAuth consent screen<br>
7. Copy the folder ID from your Google Drive Folder where you want the backups to be uploaded <br>

- `https://drive.google.com/drive/folders/FOLDER_ID`

### 2. Make sure to replace the folder paths

1. In `backup_script.py`, replace:

- SOURCE_DIR = r"PATH TO FIREFOX\PROFILES"<br>
- BACKUP_DIR = r"PATH TO BACKUP FOLDER"

2. In `upload_to_drive.py`, replace:

- folder_id = 'FOLDER ID' <br>
- backup_folder = r'PATH TO BACKUP FOLDER'

### 3. Python Dependencies 

Make sure to install these packages or run the `requirements.txt`<br>
- `google-api-python-client`<br>
- `google-auth`<br>
- `google-auth-oauthlib`<br>

--- 
### Folder Structure

```
firefox-backup/
├── backup_script.py
├── upload_to_drive.py
├── backup_bat.bat
├── credentials.json
├── token.json
└── requirements.txt
```
---

I don't even know why I'm uploading this but I am for some reason. If you ever had to go through losing your browser data and felt the need to back up your data then this might be the thing for you?

I'll be making a function to *delete the old backup zips from drive* and ig you can even use the *task scheduler or cron for automating* this.