class Customer:
    idSerial = 100000000  # 9-digit starting ID

    def __init__(self, nm, address, contact, username, password):
        Customer.idSerial += 1
        self.customerID = Customer.idSerial
        self.name = nm
        self.address = address
        self.contact = contact
        self.username = username
        self.password = password
        self.accounts = []
        self.beneficiaries = []

    def create_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)

    def add_beneficiary(self, beneficiary):
        self.beneficiaries.append(beneficiary)

    def remove_beneficiary(self, beneficiary):
        if beneficiary in self.beneficiaries:
            self.beneficiaries.remove(beneficiary)

    def display_accounts(self):
        for account in self.accounts:
            print(account)

    def __repr__(self):
        return f"Customer({self.customerID}, {self.name}, {self.username})"