class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)  # added this line

    def display(self):
        print(
            f"Hi {self.name}, you have {self.account.balance} in your available funds account")
        return f"Hi {self.name}, you have {self.account.balance} in your available funds account"


class BankAccount:
    all_instances = []
    # don't forget to add some default values for these parameters!

    def __init__(self, int_rate=.02, balance=0):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_instances.append(self)

    def make_deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def make_withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print(
                f'Sorry, but you do not have enough funds to withdraw money. Your balance: {self.balance}')
        return self

    def account_balance(self):
        print(f"Account Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print('Your account balance is negative')
        return self


user1 = User("u1", "one@gmail.com")
user2 = User("u2", "two@gmail.com")

user1.display()
user2.display()
