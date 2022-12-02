from datetime import datetime

def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
    
class TimeInterval:
    def __init(self, hrs, mins, secs):
        self.hrs = self.pad(hrs)
        self.mins = self.pad(mins)
        self.secs = self.pad(secs)
        
    def pad(self, num):
        if not isinstance(num, int):
            raise TypeError(f'{num} is not of int type')
        
        num = str(num)
        
        if len(num) > 2:
            raise Exception(f'{num} is too big')
        
        while len(num) < 2:
            num = '0' + num
        
        return num
    
    def __str__(self):
        return f'{self.hrs}:{self.mins}:{self.secs}'
    
    def __mul__(self, other):
        self.hrs = self.pad((int(self.hrs) * int(other.hrs)) % 24)
        self.mins = self.pad((int(self.mins) * int(other.mins)) % 60)
        self.secs = self.pad((int(self.secs) * int(other.secs)) % 60)
    
    def __add__(self, other):
        if isinstance(other, Time_Interval):
            self.hrs = self.pad((int(self.hrs) + int(other.hrs)) % 24)
            self.mins = self.pad((int(self.mins) + int(other.mins)) % 60)
            self.secs = self.pad((int(self.secs) + int(other.secs)) % 60)
        else:
            self.secs += other
            
            if self.secs >= 60:
                self.mins += self.secs // 60
                self.secs %= 60
            if mins >= 60:
                self.hrs += self.mins // 60
                self.mins %= 60
                # No days variable to carry over
                self.hrs %= 24
                
    def __sub__(self, other):
        if isinstance(other, TimeInterval):
            self.hrs = self.pad((int(self.hrs) - int(other.hrs)) % 24)
            self.mins = self.pad((int(self.mins) - int(other.mins)) % 60)
            self.secs = self.pad((int(self.secs) - int(other.secs)) % 60)
        else:
            if other > self.secs:
                if other > (_secs + self.mins * 60):
                    if other > (_secs + self.hrs * 60 * 60):
                        raise Exception("Can't go back in time that far")
                    self.hrs = self.hrs - (other // (60 * 60))
                    self.mins = (60 + self.mins) - (other // 60)
                else:
                    self.mins -= (other - self.secs) // 60
            else:
                self.secs = (60 + self.secs) - (other % 60)
