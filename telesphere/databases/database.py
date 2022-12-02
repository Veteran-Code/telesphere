import sqlite3
import abc

class Database(ABC):
    @classmethod
    def load_database(cls, database_location: str):
        """
            Return a connection to the database.
            Raise exception if can't find/open!
        """
        try:
            return sqlite3.connect(database_location)
        except Exception as e:
            raise Exception(str(e))
    
    @classmethod
    def get_cursor(cls, database_connection):
        return database_connection.cursor()
        
    @classmethod
    def persist_database(cls, database_connection):
        try:
            database_connection.commit()
        except Exception as e:
            raise Exception(str(e))
            
    @classmethod
    def close_database(cls, database_connection):
        try:
            database_connection.close()
        except Exception as e:
            raise Exception(str(e))
            
    @staticmethod
    def print_query(cls, results):
        for row in results:
            print(row)
            
    @staticmethod
    def write_to_xml(cls, database_connection):
        pass
        
    @staticmethod
    def write_to_csv(cls, database_connection):
        pass
        
    @staticmethod
    def write_to_json(cls, database_connection):
        pass
    
    # Validate query later
    @classmethod
    def query_database(cls, database_connection, expect_return = True, print_return = True):
        try:
            cursor = database_connection.cursor()
            result = cursor.execute(query)
            if expect_return:
                if print_return:
                    # Change to limit later
                    cls.print_query(result.fetchall())
                else:
                    return result
        except Exception as e:
            raise Exception(str(e))
                
    def __init__(self, database_name: str, database_location: str):
        self.database_name = database_name
        self.database_location = database_location
        
        try:
            self.connection = self.load_database(database_location)
        except:
            raise Exception("Could not connect to database!")
            
        self.cursor = self.get_cursor(self.connection)
        
    def commit(self):
        self.persist_database(self.connection)
        
    def __str__(self):
        loaded = True if self.connection else False
        
        return f'The database your working with is {self.database_name} and it is loaded: {loaded}'
        
    def __del__(self):
        try:
            self.close_database(self.connection)
        except:
            raise Exception("Couldn't close the database!")
        
    '''
    All subclasses should have this, but for PCPP1 the queries need to be explicit. Therefore, the abstractmethod interface wouldnt work here!
    
    @abc.abstractmethod
    def select(self, query: str):
        pass
    
    @abc.abstractmethod
    def update(self, query: str):
        pass
        
    @abc.abstractmethod
    def create_table(self, query: str):
        pass
        
    @abc.abstractmethod
    def delete_table(self, query: str):
        pass
    ''' 
