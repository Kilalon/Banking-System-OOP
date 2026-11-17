Total_Accounts = 0
usernames = {}

class Account:


    def __init__(self, Account_name, Full_name,Password, age, Balance, Home_Adress):
        self.Account_name = Account_name
        self.Full_name = Full_name
        self.Password = Password
        self.age = age
        self.Balance = Balance
        self.Home_Adress = Home_Adress
        self.Transactions = []
        self.entry = False
        self.inside_account = False

    def login(self, inputed_name, inputed_Password):
        if inputed_name == self.Account_name and inputed_Password == self.Password:
            print("Login Successful!")
            self.entry = True
            self.inside_account = True
        else:
            print("Login Unsuccessful!")
            print('Access Denied!')

    def show_balance(self):
        print(f"Your current Balance is: ${self.Balance}")

    def deposit(self, amount):
        Initial = self.Balance
        self.Balance += amount
        self.Transactions.append(self.Balance - Initial)
        print(f"Your current Balance is: ${self.Balance}")

    def withdraw(self, amount):
        Initial = self.Balance
        self.Balance -= amount
        self.Transactions.append(self.Balance - Initial)
        print(f"Your current Balance is: ${self.Balance}")

    def Transaction_list(self):
        print(self.Transactions)

    def Log_out(self):
        self.entry = False
        self.inside_account = False
        print("Logout Successful!")


def Create_Account():
    global Total_Accounts
    global usernames
    Full_name = input("Enter your full name: ")
    Account_name = input("Enter the Account name that you would like to re-log in with: ")
    Password = input("Enter your Password: ")
    age = int(input("Enter your age (Age must be 21 or older): "))
    Balance = float(input("Enter your initial balance (Has to be be at least $50): "))
    Home_Adress = input("Enter your home adress: ")
    if age < 21: print("Invalid age!!")
    elif Balance < 50: print("Invalid Initial Balance!!")
    else:
        Total_Accounts += 1
        ACC_Name = Account_name
        Account_name = Account(Account_name, Full_name,Password, age, Balance, Home_Adress)
        usernames.update({ACC_Name:Account_name})

while True:
    options = input("Would you like to: Create Account or log into an account or Exit? (create / log in / exit): ").lower()
    match options:
        case 'admin':
            print(f"Total number of accounts registered is {Total_Accounts}")
            print(usernames)
            specific_user = input("Specific account you would like to see its details?: ")
            if specific_user in usernames:
                entry = usernames[specific_user]
                print(f"Account name: {entry.Account_name}")
                print(f"Full Name: {entry.Full_name}")
                print(f"Account Password: {entry.Password}")
                print(f"User Age: {entry.age}")
                print(f"Account Balance: {entry.Balance}")
                print(f"User's Home Adress: {entry.Home_Adress}")
                print(f"User Transactions: {entry.Transactions}")
        case 'exit':
            break
        case 'create':
            Create_Account()
        case 'log in':
            inputed_name = input("Enter the Account name: ")
            inputed_password = input("Enter your Password: ")
            try:
                entry = usernames[inputed_name]
                entry.login(inputed_name, inputed_password)

                if entry.entry:
                    while entry.inside_account:
                        user_options = input("Would you like to (show balance / deposit / withdraw / transaction list / log out)?: ").lower()
                        match user_options:
                            case 'log out':
                                entry.Log_out()
                                break
                            case 'show balance':
                                entry.show_balance()
                            case 'deposit':
                                amount = float(input('Enter the amount you would like to deposit: '))
                                entry.deposit(amount)
                            case 'withdraw':
                                amount = float(input('Enter the amount you would like to withdraw: '))
                                entry.withdraw(amount)
                            case 'transaction list':
                                entry.Transaction_list()
                else: print("Faulty attempt!")
            except:
                print("Account not found!")
            
print("Have a nice Day")