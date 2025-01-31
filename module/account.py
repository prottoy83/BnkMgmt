from transaction import *


class Account:
    idSerial = 10000000000  # 11-digit starting ID

    def __init__(self, customerID, balance, type):
        Account.idSerial += 1
        self.accountID = Account.idSerial
        self.customerID = customerID
        self.balance = balance
        self.type = type
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction = Transaction(amount, self.accountID, "Deposit")
            self.transactions.append(transaction)
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            transaction = Transaction(amount, self.accountID, "Withdrawal")
            self.transactions.append(transaction)
        else:
            raise ValueError("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

    def __repr__(self):
        return f"Account({self.accountID}, Balance: {self.balance}, Type: {self.type})"


class Beneficiary:
    idSerial = 100000000000  # 12-digit starting ID

    def __init__(self, name, customerID, accountNumber):
        Beneficiary.idSerial += 1
        self.beneficiaryID = Beneficiary.idSerial
        self.name = name
        self.customerID = customerID
        self.accountNumber = accountNumber

    def __repr__(self):
        return f"Beneficiary({self.beneficiaryID}, {self.name}, Account: {self.accountNumber})"