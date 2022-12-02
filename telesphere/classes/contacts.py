import re
import abc

class Contact:
    def __init__(self, name, phone_number = None, email = None):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        
    def __str__(self):
        return f'{name}: phone number - {self.phone_number}, email - {self.email}'

class ContactCacheAbstract(abc.ABC):
    # Add list structure so you can run a binary search
    self.contacts = {}
    
    @classmethod
    def load_contacts_from_csv(cls, file_location: str):
        try:
            with open(file_location, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    try:
                        self.phone_contacts.append(Contact(*row))
                    except:
                        raise Exception("Not a phone contact instance!")
        except:
            raise Exception("Could not open the csv file!")
            
    @classmethod
    def search_contacts(cls, name = None, phone_number = None, email = None):
        # Run a binary search here!
        found = []
        idx = 0
        
        while idx < len(cls.contacts):
            contact = cls.contacts[idx]
            
            if name:
                if re.search(name, contact.name, re.IGNORECASE):
                    found.append(contact)
            elif phone_number:
                if re.search(phone_number, contact.phone_number, re.IGNORECASE):
                    found.append(contact)
                    
            idx += 1
        
        if found is None:
            print("No contacts found!")
        else:
            return found
    
    @staticmethod
    def flush(cls, option):
        # Write to csv, xml, and sqlite3
        pass
    
    def __init__(self):
        pass
        
    @abc.abstractmethod
    def insert_contacts(self, name = None, phone_number = None, email = None):
        pass
    
class ContactCache(ContactCacheAbstract):
    def __init__(self, phone_contacts: list = []):
        if isinstance(phone_contacts, list):
            for item in phone_contacts:
                if isinstance(item, PhoneContact) is False:
                    raise Exception("Must be PhoneContacts instances only")
            self.phone_contacts = phone_contacts
        else:
            raise Exception("Phone contacts must be a list of PhoneContact instances!")
            
    def insert_contacts(self, name = None, phone_number = None, email = None):
        pass

