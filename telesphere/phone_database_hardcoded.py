import time

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
        """
            Database location must have / at end
            Database name must have .db at end
        """
        self.database_name = database_name
        self.database_location = database_location
        
        self.database = f'{self.database_location}{self.database_name}'
        
        self.conn = self.connect()
        self.cursor = self.get_cursor()
        
    def __str__(self):
        return f'{self.database_name} is active on {int(time.time())}'
        
    def connect(self):
        return sqlite3.connect(self.database_location)
        
    def close(self):
        self.conn.close()
        
    def commit(self):
        self.conn.commit()
        
    def get_cursor(self):
        return self.conn.cursor()
        
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
            
    def print_rows(self, rows):
        for row in rows:
            print(row)
    
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
            
    def __del__(self):
        try:
            self.close()
        except Exception as e:
            print(e)

