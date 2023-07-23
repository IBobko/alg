import pickle

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/contacts',
          'https://www.googleapis.com/auth/drive.metadata'
          'https://www.googleapis.com/auth/spreadsheets']
credentials_file = 'credentials.json'
token_file = 'token.pickle'


class GoogleCloud:
    def __init__(self):
        self.credentials = self.load_credentials()

    def load_credentials(self):
        """
        Loads the Google API credentials.

        Returns:
            The loaded credentials object.
        """
        flow = InstalledAppFlow.from_client_secrets_file(
            credentials_file,
            scopes=SCOPES,
            redirect_uri="https://localhost"
        )

        try:
            # Try to load the saved credentials from file
            with open(token_file, 'rb') as token:
                credentials = pickle.load(token)
        except FileNotFoundError:
            credentials = flow.run_local_server()
            with open(token_file, 'wb') as token:
                pickle.dump(credentials, token)

        return credentials

    def get_sheet_service(self):
        """
        Builds and returns a Google Sheets API service using the loaded credentials.

        Returns:
            A Google Sheets API service object.
        """
        return build('sheets', 'v4', credentials=self.credentials)

    def build_people_service(self):
        """
        Builds and returns a Google People API service using the loaded credentials.

        Returns:
            A Google People API service object.
        """
        return build('people', 'v1', credentials=self.credentials)
