import phonenumbers as phonenumbers

class GoogleSheets:
    GOOGLE_SHEET_ID = "1qTSiFVTDHvL40GX7BLWnLoQhkSZVSU1xT4u_qRPjOJo"

    def __init__(self, google_cloud, contacts_service):
        """
        Initializes a GoogleSheets object.

        Args:
            google_cloud: An instance of the GoogleCloud class for accessing Google APIs.
            contacts_service: An instance of the ContactsService class for retrieving contacts.
        """
        self.google_cloud = google_cloud
        self.contacts_service = contacts_service

    def save_contacts_to_sheet(self):
        """
        Retrieves contacts from the ContactsService and saves them to a Google Sheets document.
        """
        sheet_service = self.google_cloud.get_sheet_service()
        contacts = self.contacts_service.get_contacts()

        values = []
        for contact in contacts:
            names = contact.get('names', [])
            name = ''
            if names:
                name = names[0].get('displayName')
            email_addresses = contact.get('emailAddresses', [])
            email = ''
            if email_addresses:
                email = email_addresses[0].get('value')
            phone_numbers = contact.get('phoneNumbers', [])
            phone_number = ''
            if phone_numbers:
                phone_number = phone_numbers[0].get('value')

            formatted_number = ''
            try:
                parsed_number = phonenumbers.parse(phone_number, None)
                if phonenumbers.is_valid_number(parsed_number):
                    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                    print("Input number: ", phone_number)
                    print("Formatted number: ", formatted_number)
                    print()
                else:
                    print("Invalid number: ", phone_number)
                    print()
            except phonenumbers.phonenumberutil.NumberParseException:
                print("Error parsing number: ", phone_number)
                print()

            values.append(
                [contact.get('etag'), contact.get('resourceName'), name, phone_number, formatted_number, email])

        body = {'values': values}
        sheet_service.spreadsheets().values().update(
            spreadsheetId=GoogleSheets.GOOGLE_SHEET_ID, range='Sheet1!A1', valueInputOption='RAW', body=body).execute()

        print('The contacts have been successfully saved in the Google Sheets document.')
