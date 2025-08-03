import os
import io
from googleapiclient.http import MediaIoBaseUpload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# If modifying these SCOPES, delete token.json
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def upload_to_drive(file_path):

    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    folder_id = 'FOLDER ID' # folder id of the google drive folder where you wanna save the zip

    file_metadata = {
        'name': os.path.basename(file_path),
        'mimeType': 'application/zip',
        'parents': [folder_id]
    }

    CHUNK_SIZE = 5 * 1024 * 1024  # 5MB chunks cuz upload limit issue 
    media = MediaIoBaseUpload(
        io.FileIO(file_path, 'rb'),
        mimetype='application/zip',
        chunksize=CHUNK_SIZE,
        resumable=True
    )

    request = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Upload progress: {int(status.progress() * 100)}%")

    print(f"Uploaded {file_path} to Google Drive (File ID: {response.get('id')})")


if __name__ == '__main__':
    backup_folder = r'PATH TO BACKUP FOLDER'
    latest_file = max(
        [os.path.join(backup_folder, f) for f in os.listdir(backup_folder)],  # only the latest file
        key=os.path.getctime
    )
    upload_to_drive(latest_file)
