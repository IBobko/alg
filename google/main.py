from contact_service import ContactsService
from google_sheets import GoogleSheets
from google_cloud import GoogleCloud


def main():
    google_cloud = GoogleCloud()
    contacts_service = ContactsService(google_cloud)
    google_sheets = GoogleSheets(google_cloud, contacts_service)
    google_sheets.save_contacts_to_sheet()


if __name__ == '__main__':
    main()
