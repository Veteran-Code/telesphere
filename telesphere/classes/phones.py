import abc
import time
from datetime import datetime
    
from pkg.classes.imei import ImeiHandler
from pkg.utils.timespace import TimeInterval

# Write to database immediately
class Phone(abc.ABC, TimeInterval):
    counter = 0

    @classmethod
    def call(cls, number):
        # Fix time interval to utilize days too
        started = TimeInterval(*cls.get_time())
        message = 'Calling {} using own number {} at {}'.format(number, self.number, start)
        return message
    
    # Log here
    @classmethod
    def end_call(cls, number, started)
        ended = TimeInterval(*cls.get_time())
        message = 'Ended call with {} using number {} at {}.\nThis lasted {}.'.format(number, self.number, ended - started)
        return message
    
    @staticmethod
    def get_time(cls):
        # # Fix time interval to utilize days too
        # return datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
        _time = datetime.now().strftime("%H:%M:%S.%f").split(":")
        hours = _time[0]
        mins = _time[1]
        secs = int(_time[2])
        
        return hours, mins, secs
        
    def __init__(self, number):
        self.number = number
        self.imei_number = [imei_number for imei_number in ImeiHandler(amount=1)][0]
        
        Phone.counter += 1
    
    @abc.abstractmethod    
    def turn_on(self):
        # return f'mobile phone {self.number}'
        pass
        
    @abc.abstractmethod
    def turn_off(self):
        # return f'mobile phone is turned off'
        pass

class FixedPhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        FixedPhone.last_SN += 1
        self.SN = 'FP-{}'.format(FixedPhone.last_SN)
        
    # Should just refer to the database information since this won't change. Use class name to check
    @check_location
    def turn_on(self):
        pass
        
    # Same as above
    @check_location
    def turn_off(self):
        pass


class MobilePhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        MobilePhone.last_SN += 1
        self.SN = 'MP-{}'.format(MobilePhone.last_SN)
        
    @check_location
    def turn_on(self):
        pass
        
    @check_location
    def turn_off(self):
        pass
