class BankAccount:
    def init (self,account_holder,initial_balance=0,atm_pin=None): 
        self.account_holder = account_holder  
        self.balance = initial_balance 
        self.atm_pin = atm_pin

    def check_balance(self):
        print(f"current balance of {self.account_holder} is {self.balance}")

    def validate_pin(self):
        enterd_pin = int(input("Enter your Transaction Pin:")) 
        return enterd_pin == self.atm_pin

# Here we taking user confirmation if he want to change pin or not 
# Then by selecting option-4, user can change his pin.
    def change_pin(self,new_pin):
        confirm = input("Confirm? Y/N: ") 
        if confirm in ("Y", "y"):
            enterd_pin = new_pin
            print("Congratulation...!! Your new Pin is updated.") 
        else:
            print("pin change process is cancelled...try again...")

# Deposit restricted as multiple of 100
# Here if user deposit amount is multiple of 100 then it will not add to its current balance.
    def deposit(self, amount): 
        if self.atm_pin is None:
           print("your transaction Pin is not set. Please set your Transaction Pin.")

        if amount > 0:
           if amount%100 != 0: 
              self.balance += amount
              print(f"Deeposit amount is Rs.{amount} \nCurrent balance is Rs.{self.balance}")
           else:
               print("Deposit amount must not be multiplication of 100.")
        else:    
            print("Deposit amount must be greater than Zero.")        

# our withdraw amount limit is 10000 
# our default charge amount is 500
    def withdraw(self, amount, charge_amount=500): 
        if self.atm_pin is None:
            print("your transaction Pin is not set. Please set your Transaction Pin.")

        if 0 < amount <= self.balance:
            if amount <= 10000 and self.validate_pin: 
               self.balance = self.balance-charge_amount
               print(f"Withdraw amount is Rs.{amount} \nCurrent balance is Rs.{self.balance}")
            elif amount > 10000:
               self.balance = self.balance - charge_amount
               print(f"charged 500 .current balance is {self.balance} .Your withdraw amount exceeds ATM limit")
            else:
               print("withdraw amount exceeds ATM limit or invalid PIN")
        else:
           print("Invalid withdraw amount.")

def main():
    print("Welcome to our banking service.") 
    try:
        account_holder = input("Enter account holder name: ") 
        initial_balance = float(input("Enter your initial balance: ")) 
        atm_pin = int(input("Set your Transaction Pin: "))
        user_account = BankAccount(account_holder, initial_balance, atm_pin) 
        while True:
            print("\nSelect an option:") 
            print("1. Deposit") 
            print("2. Withdraw") 
            print("3. Check Balance") 
            print("4. change_pin") 
            print("5. Exit")

            choice=input("enter your choice:")

            if choice == "1": 
                try:
                  amount = float(input("Enter deposit amount:")) 
                  user_account.deposit(amount)
                except ValueError:
                  print("Please Enter a Valid Amount")

            elif choice == "2":
                try:
                    amount = float(input("Enter withdraw amount:")) 
                    user_account.withdraw(amount)
                except ValueError:
                    print("Please Enter a Valid Amount")

            elif choice == "3": 
               user_account.check_balance()

            elif choice == "4": 
               try:
                   new_pin = float(input("Enter your new pin:")) 
                   user_account.change_pin(new_pin)
               except ValueError: 
                   print("try again.")

            elif choice == "5":
               print("Thank you for using our banking services!") 
               break

            else:
               print("Please select a valid option.")

    except ValueError:
        print("Please valid account information.")

if __name__ == " __main__ " : 
     main()
