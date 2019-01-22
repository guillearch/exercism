import threading

class BankAccount(object):

    lock = threading.Lock()

    def __init__(self):
        self.is_open = False

    def open_required(func):
        def wrapper(self, *args):
            if not self.is_open:
                raise ValueError('Please, open your account first.')
            return func(self, *args)
        return wrapper

    def open(self):
        if self.is_open:
            raise ValueError('Please, close your account first.')
        self.balance = 0
        self.is_open = True

    @open_required
    def get_balance(self):
        return self.balance

    @open_required
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('You cannot deposit a negative amount.')
        with self.lock:
            self.balance += amount

    @open_required
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('You cannot withdraw a negative amount.')
        with self.lock:
            if amount > self.balance:
                raise ValueError('You do not have enough money.')
            self.balance -= amount

    @open_required
    def close(self):
        self.is_open = False
