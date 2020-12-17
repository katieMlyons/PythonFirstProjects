class Account:

    def __init__(self, filepath):
        with open(filepath,"r") as file:
            self.filepath = filepath
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, "w") as file:
            file.write(str(self.balance))

class Checking(Account):

    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

jacks_checking = Checking("Jack.txt", 1)
jacks_checking.transfer(100)
jacks_checking.commit()
print(jacks_checking.balance)

johns_checking = Checking("John.txt", 1)
johns_checking.transfer(100)
johns_checking.commit()
print(johns_checking.balance)