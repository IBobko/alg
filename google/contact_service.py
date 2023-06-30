class ContactsService:
    def __init__(self, google_cloud):
        self.google_cloud = google_cloud

    def get_contacts(self):
        """
        Retrieves a list of contacts from the Google People API.

        Returns:
            A list of contacts containing information such as names, email addresses, and phone numbers.
        """
        service = self.google_cloud.build_people_service()
        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=2000,
            personFields='names,emailAddresses,phoneNumbers'
        ).execute()

        contacts = results.get('connections', [])
        return contacts

    def get_contact(self, contact_resource_name):
        """
        Retrieves a specific contact from the Google People API.

        Args:
            contact_resource_name: The resource name of the contact to retrieve.

        Returns:
            The contact object containing information such as names, email addresses, and phone numbers.
        """
        service = self.google_cloud.build_people_service()
        contact = service.people().get(
            resourceName=contact_resource_name,
            personFields='names,emailAddresses,phoneNumbers'
        ).execute()
        return contact

    def update_contact(self, contact_resource_name, updated_contact):
        """
        Updates a specific contact in the Google People API.

        Args:
            contact_resource_name: The resource name of the contact to update.
            updated_contact: The updated contact object with modified information.

        Returns:
            The updated contact object.
        """
        service = self.google_cloud.build_people_service()

        updated_contact = service.people().updateContact(
            resourceName=contact_resource_name,
            updatePersonFields='names,emailAddresses,phoneNumbers',
            body=updated_contact
        ).execute()

        return updated_contact
