from account import*
from customer import *
from transaction import*

class Employee:
    idSerial = 10000  # 5-digit starting ID

    def __init__(self, name, address, contact):
        Employee.idSerial += 1
        self.employeeID = Employee.idSerial
        self.name = name
        self.address = address
        self.contact = contact
        self.salary = 0

    def update_contact_info(self, new_contact):
        self.contact = new_contact

    def view_salary(self):
        return self.salary

    def __repr__(self):
        return f"Employee({self.employeeID}, {self.name}, Contact: {self.contact})"


class Admin(Employee):
    def __init__(self, name, address, contact, designation):
        super().__init__(name, address, contact)
        self.designation = designation

    def add_employee(self, employee):
        """Registers a new employee."""
        print(f"Employee {employee.name} added successfully.")

    def remove_employee(self, employee_id):
        """Removes an employee from the system."""
        print(f"Employee with ID {employee_id} removed successfully.")

    def update_employee_salary(self, employee_id, new_salary):
        """Updates an employee's salary."""
        print(f"Salary updated for Employee ID {employee_id}.")

    def __repr__(self):
        return f"Admin({self.employeeID}, {self.name}, {self.designation})"


class Teller(Employee):
    def __init__(self, name, address, contact, designation):
        super().__init__(name, address, contact)
        self.designation = designation

    def process_deposit(self, account, amount):
        """Handles customer deposits."""
        try:
            account.deposit(amount)
            print(f"Deposit of {amount} successful for Account {account.accountID}.")
        except ValueError as e:
            print(f"Error: {e}")

    def process_withdrawal(self, account, amount):
        """Handles customer withdrawals."""
        try:
            account.withdraw(amount)
            print(f"Withdrawal of {amount} successful for Account {account.accountID}.")
        except ValueError as e:
            print(f"Error: {e}")

    def __repr__(self):
        return f"Teller({self.employeeID}, {self.name}, {self.designation})"
