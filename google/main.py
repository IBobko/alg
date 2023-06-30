import argparse

from contact_service import ContactsService
from google_cloud import GoogleCloud
from google_sheets import GoogleSheets


def main():
    parser = argparse.ArgumentParser(description='Script for performing various operations.')
    parser.add_argument('command', choices=['save_contacts', 'other_command'], help='The command to execute')

    args = parser.parse_args()
    command = args.command

    google_cloud = GoogleCloud()
    contacts_service = ContactsService(google_cloud)
    google_sheets = GoogleSheets(google_cloud, contacts_service)

    if command == "save_contacts":
        print("save_contacts:", command)
        google_sheets.save_contacts_to_sheet()
    elif command == "other_command":
        print("other_command:", command)
        pass
    else:
        print("Unknown command:", command)


if __name__ == '__main__':
    main()
