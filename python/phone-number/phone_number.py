import re


class Phone(object):
    def __init__(self, phone_number):
        num = re.sub(r'[\D]', '', phone_number)
        if re.fullmatch(r'^1?([2-9]\d{2})([2-9]\d{2})(\d{4})$', num):
            if num.startswith('1'):
                self.number = num[1:]
            else:
                self.number = num
        else:
            raise ValueError('Invalid phone number.')

    def number(self):
        return self.number

    def pretty(self):
        return f'({self.number[:3]}) {self.number[3:6]}-{self.number[6:]}'

    @property
    def area_code(self):
        return self.number[:3]
