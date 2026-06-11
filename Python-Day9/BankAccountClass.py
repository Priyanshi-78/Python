#Create Bank Account Class
class BankAccount:
    def __init__(self, account_no,balance):
        self.account_no = account_no
        self.balance = balance
    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)

account1 = BankAccount("543211", 10000)
account2 = BankAccount("678912", 2000)
account3 = BankAccount("987613", 500)

account1.display()
account2.display()
account3.display()