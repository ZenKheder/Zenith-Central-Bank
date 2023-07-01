import random
import string
import json

# Mother Class
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = balance
    
    def __str__(self):
        return f"Bank Account #{self._account_number}: Balance - {self._balance}"
    
    @classmethod
    def get_bank_name(cls):
        return "Zenith Central Bank"
    
    @staticmethod
    def is_valid_account_number(account_number):
        return len(str(account_number)) == 6
        
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance += amount
        
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        if self._balance >= amount:
            self._balance -= amount
        else:
            raise ValueError("Insufficient balance")    

    @staticmethod
    def generate_account_number():
        return "".join(random.choices(string.digits, k=6))

def read_data_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

def write_data_to_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file)

def account_exists(account_number, data):
    for account in data:
        if account['account_number'] == account_number:
            return account
    return None

def open_account():
    print("Welcome to Zenith Central Bank!")
    account_check = input("Do you have an existing account? (yes/no): ")

    data = read_data_from_json('accounts.json')

    if account_check.lower() == "yes":
        account_number = input("Enter your account number: ")
        existing_account = account_exists(account_number, data)

        if existing_account:
            name = existing_account['name']
            print(f"Account found!, welcome back {name}")
            print(f"Your current balance is: {existing_account['balance']}")
            
            while True:
                # Implement the options for existing account here
                option = input("Choose an option: deposit, withdraw, or exit: ").lower()
                
                if option == 'deposit':
                    amount = float(input("Enter the deposit amount: "))
                    existing_account['balance'] += amount
                    print(f"Deposit of {amount} successful. Your new balance is: {existing_account['balance']}")

                elif option == 'withdraw':
                    amount = float(input("Enter the withdrawal amount: "))
                    if existing_account['balance'] >= amount:
                        existing_account['balance'] -= amount
                        print(f"Withdrawal of {amount} successful. Your new balance is: {existing_account['balance']}")
                    else:
                        print("Insufficient balance.")
                elif option == 'exit':
                    write_data_to_json('accounts.json', data)
                    print("Thank you for using Zenith Central Bank. Goodbye!")
                    break
                else:
                    print("Invalid option. Please choose a valid option.")

        else:
            print("Account number not found. Please check the account number.")

    elif account_check.lower() == "no":
        creation = input("Do you want to create an account? (yes/no): ")
        if creation.lower() == "yes":
            passport_number = input("Please enter your passport number: ")
            name = input("Please enter your name: ")
            initial_balance = float(input("Enter initial balance: "))
            account_number = BankAccount.generate_account_number()
            new_account = BankAccount(account_number, initial_balance)
            account_data = {
                'account_number': account_number,
                'passport_number': passport_number,
                'name': name,
                'balance': initial_balance
            }
            data.append(account_data)
            write_data_to_json('accounts.json', data)
            print(f"Thank you for choosing Zenith Central Bank! Your account number is: {account_number}")
            print(f"Account Holder: {name}")
            print(f"Passport Number: {passport_number}")
            print(new_account)
        else:
            print("Account creation cancelled")    

    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Example usage:
if __name__ == "__main__":
    try:
        open_account()
    except ValueError as e:
        print(f"Error: {e}")
