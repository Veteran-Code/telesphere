from telesphere.database.abstract_database import Database

class PhoneDatabase(Database):
    create_phone_query = """CREATE TABLE IF NOT EXISTS phones (
    id INTEGER PRIMARY KEY,
    number INTEGER NOT NULL,
    imei INTEGER NOT NULL,
    last_known_hit_latitude REAL NOT NULL,
    last_known_hit_longitude REAL NOT NULL,
    user_uuid TEXT NOT NULL);"""
    
    insert_information = "INSERT INTO phones (number, imei, last_known_hit_latitude, last_known_hit_longitude, user_uuid) VALUES (?,?,?,?,?)"
    
    get_all_information = "SELECT * FROM phones"
    
    update_gps_coords = "UPDATE phones SET last_known_hit_latitude = ?, last_known_hit_longitude = ? WHERE number = ?;"
    
    delete_number = "DELETE FROM phones WHERE number = ?"
    
    def __init__(self, database_name: str, database_location: str):
        super().__init__(database_name, database_location)
        
    def create_table(self):
        try:
            self.cursor.execute(self.create_phone_query)
            self.commit()
            return True
        except:
            return False
        
    def insert(self, number: int, imei: int, last_known_latitude: float, last_known_longitude: float, user_uuid: str):
        try:
            self.cursor.execute(self.insert_information, (number, imei, last_known_latitude, last_known_longitude, user_uuid))
            return True
        except:
            return False

    def select(self):
        return self.cursor.execute(self.get_all_information)
    
    def update(self, number: int, latitude: float, longitude: float):
        try:
            self.cursor.execute(self.update_gps_coords, (latitude, longitude, number))
            self.commit()
            return True
        except:
            return False
        
    def delete_table(self, number: int):
        try:
            self.cursor.execute(self.delete_number, (number,))
            self.commit()
            return True
        except:
            return False
