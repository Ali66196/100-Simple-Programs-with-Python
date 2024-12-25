# ATM Simulation

class ATM:
    def __init__(self, balance):
        self.balance = balance  # موجودی حساب

    # تابع برای واریز پول
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} Toman deposited into account.")
        else:
            print("Amount must be greater than zero.")

    # تابع برای برداشت پول
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} Toman withdrawn from account.")
        else:
            print("Insufficient balance!")

    # تابع برای نمایش موجودی حساب
    def check_balance(self):
        print(f"Your account balance is: {self.balance} Toman")

# ایجاد شیء از دستگاه خودپرداز با موجودی اولیه 100000 تومان
atm = ATM(100000)

# منوی دستگاه خودپرداز
while True:
    print("\n1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Exit")
    
    choice = input("Please select an option: ")
    
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == "3":
        atm.check_balance()
    elif choice == "4":
        print("Exiting the system...")
        break
