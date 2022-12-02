import traceback
    
class FakeImei(Exception):
    pass

def validate_check_digit(func):
    def internal_wrapper(*args, **kwargs):
        check_digit = func(*args, **kwargs)
        
        if check_digit is not 0:
            raise FakeImei("The check digit function does not check out!")
        
    return internal_wrapper

class Imei:
    # IMEIs will be generated based on the first 8 digits (TAC; the number
    #   used to identify the model) and the next 2-6 digits (partial serial #).
    #   The final, 15th digit, is the Luhn algorithm check digit.
    
    def __init__(self, tac_number: int, serial_number: int, alphabet: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        self.number = int(f'{tac_number}{serial_number}')
        self.alphabet = alphabet
        self.alphabet_length = len(self.alphabet)
        
        self.checksum_number = self.checksum()
        
        self.check_digit = self.calc_check_digit()
        
    def __str__(self):
        return f'IMEI Number is {self.get_imei_number()} with a checksum of {self.checksum_number}.'
        
    def checksum(self):
        """
            Calculate the Luhn checksum over the provided number.
            The checksum is returned as an int.
            Valid numbers should have a checksum of 0.
        """
        
        number = tuple(self.alphabet.index(i) for i in reversed(str(number)))
        
        return (sum(number[::2]) + sum(sum(divmod(i * 2, n)) for i in number[1::2])) % self.alphabet_length
    
    @validate_check_digit
    def calc_check_digit(self):
        check_digit = self.checksum(self.number + self.alphabet[0])
        
        return self.alphabet[-1 * check_digit]
        
    def get_imei_number(self):
        return f'{self.number}{self.check_digit}'
