from telesphere.database.abstract_database import Database

# Figure out what package I finally import
from ... import email_validator

class ContactDatabase(Database):
    create_contact_query = """CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    uuid TEXT NOT NULL,
    number INTEGER,
    email TEXT);"""
    
    insert_information = "INSERT INTO contacts (uuid, number, email) VALUES (?,?,?)"
    
    get_all_information = "SELECT * FROM contacts"
    
    update_number = "UPDATE contacts SET number = ? WHERE uuid = ?;"
    update_email = "UPDATE contacts SET email = ? WHERE uuid = ?;"
    update_both = "UPDATE contacts SET number = ?, email = ? WHERE uuid = ?;"
    
    delete_uuid = "DELETE FROM contacts WHERE uuid = ?"
    
    options = ["number", "email", "both"]
    
    def __init__(self, database_name: str, database_location: str):
        super().__init__(database_name, database_location)
        
    def create_table(self):
        try:
            self.cursor.execute(self.create_contact_query)
            self.commit()
            return True
        except:
            return False
        
    def insert(self, uuid: str, number: int, email: str):
        try:
            if email_validator(email):
                self.cursor.execute(self.insert_information, (uuid, number, email))
                return True
            else:
                raise Exception("Can't do it with a fake email!")
        except:
            return False

    def select(self):
        return self.cursor.execute(self.get_all_information)
    
    # options: [number, email]
    def update(self, option: str, **kwargs):
        try:
            idx = options.index(option)
            
            if idx == 0:
                self.cursor.execute(self.update_number, (kwargs['number'], kwargs['uuid']))
            elif idx == 1:
                self.cursor.execute(self.update_email, (kwargs['email'], kwargs['uuid']))
            else:
                self.cursor.execute(self.update_both, (kwargs['number'], kwargs['email'], kwargs['uuid']))
            self.commit()
            return True
        except:
            return False
        
    def delete_table(self, uuid: str):
        try:
            self.cursor.execute(self.delete_uuid, (uuid,))
            self.commit()
            return True
        except:
            return False
