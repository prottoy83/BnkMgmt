from datetime import datetime
from account import*
from customer import *
from employee import*


class Transaction:
    idSerial = 100000000000000  # 15-digit starting ID

    def __init__(self, amount, accountID, type):
        Transaction.idSerial += 1
        self.transactionID = Transaction.idSerial
        self.amount = amount
        self.accountID = accountID
        self.type = type
        self.timeStamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return f"Transaction({self.transactionID}, {self.type}, Amount: {self.amount}, Time: {self.timeStamp})"