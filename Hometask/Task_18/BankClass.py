class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * (self.interest_rate / 100)
        self._balance += interest


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self._balance < 0:
            print(f"Overdraft letter sent for account number {self._account_number}")


class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                self.accounts.remove(account)
                return True
        return False

    def pay_dividend(self, amount):
        for account in self.accounts:
            account.deposit(amount)

    def update(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()



if __name__ == '__main__':

    # Test the implementation
    bank = Bank()

    # Open some accounts
    account1 = Account.create_account("001")
    savings_account = SavingsAccount(1000, "002", 5)  # Initial balance: $1000, Interest rate: 5%
    current_account = CurrentAccount(500, "003", -1000)  # Initial balance: $500, Overdraft limit: $1000

    bank.open_account(account1)
    bank.open_account(savings_account)
    bank.open_account(current_account)

    # Test update method
    print("Before update:")
    for account in bank.accounts:
        print(account)

    bank.update()

    print("\nAfter update:")
    for account in bank.accounts:
        print(account)

    # Close an account
    bank.close_account("001")
    print("\nAfter closing an account:")
    for account in bank.accounts:
        print(account)

    # Pay dividend
    bank.pay_dividend(100)
    print("\nAfter paying dividend:")
    for account in bank.accounts:
        print(account)