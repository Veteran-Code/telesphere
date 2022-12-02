import logging

from pkg.classes.imei import Imei

class ImeiHandler:
    FORMAT = '%(name)s - IMEI number => %(levelname)s - %(message)s'
    logger = logging.getLogger(__name__)
    # Make location for this in init!!!
    handler = logging.FileHandler("/usr/logging/imei_created.log", mode="w")
    formatter = logging.Formatter(cls.FORMAT)
    
    cls.handler.setLevel(logging.INFO)
    cls.handler.setFormatter(cls.formatter)
    cls.logger.addHandler(cls.handler)
    
    def __init__(self, amount: int = 1):
        self.amount_left = amount
        
    def __iter__(self):
        return self
        
    def __next__(self):
        found = False
        count = 0
        
        while not found:
            count += 1
            tac_number = int(''.join([str(randint(0,9)) for _ in range(8)]))
            serial_number = int(''.join([str(randint(0,9)) for _ in range(6)]))
            
            try:
                new_imei = Imei(tac_number, serial_number)
                found = True
                
                self.logger.info(f'Created a new IMEI - {tac_number}{serial_number} at {get_timestamp()}')
            except FakeImei as e:
                self.logger.warning(f'{e} for {tac_number}{serial_number}')
            except Exception as e:
                self.logger.critical(f'{e} didn\'t catch {tac_number}{serial_number}')
                
            if count == 100:
                raise Exception("ImeiHandler is not working properly!")
        
        return new_imei
