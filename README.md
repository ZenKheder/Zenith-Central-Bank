# Zenith-Central-Bank
"Zenith Central Bank" is a simple Python project that simulates a basic banking system. It allows users to create new bank accounts, check their existing accounts, deposit money, and withdraw funds. The project uses a local JSON database to store account information, making it easy to manage multiple accounts.

## Features
## Account Creation:
Users can create a new bank account by providing their passport number, name, and an initial balance.
## Account Lookup:
Existing users can check their account balance by providing their account number.
## Deposit and Withdraw:
Account holders can deposit money into their accounts or make withdrawals, provided they have sufficient balance.
## Account Number Validation:
The system ensures that each account number generated is unique and consists of six digits.

Bank Information: The bank's name, "Zenith Central Bank," is accessible through a class method.


## Getting Started
To run the project, follow these steps:

Install Python (if you haven't already) on your local machine.
Clone this repository to your local machine.
Open the terminal/command prompt and navigate to the project directory.
Run the script using the following command: python bank.py
## How it Works
The project utilizes object-oriented programming (OOP) concepts in Python to create a BankAccount class. This class represents a bank account and contains methods for managing the account's balance, generating account numbers, and checking the validity of account numbers.

The banking operations, such as account creation, deposit, and withdrawal, are handled in the open_account function. This function interacts with the user to determine if they already have an account or wish to create a new one. It reads and writes account data using a local JSON database, 'accounts.json,' to store the account information.

## Future Improvements
While "Zenith Central Bank" is a basic project suitable for beginners, there are several potential enhancements that can be implemented:

Implementing user authentication and password protection for increased security.
Adding error handling and validation for user inputs to prevent unexpected behavior.
Enabling more advanced banking features, such as transaction history and account management options.
Creating a simple graphical user interface (GUI) for a more user-friendly experience.
Contribution
Contributions to the project are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.
