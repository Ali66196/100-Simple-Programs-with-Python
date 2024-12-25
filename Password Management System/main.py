# سیستم مدیریت رمز عبور

class PasswordManager:
    def __init__(self):
        self.passwords = {}  # دیکشنری برای ذخیره رمزهای عبور

    # تابع برای اضافه کردن رمز عبور
    def add_password(self, website, password):
        self.passwords[website] = password
        print(f"Password for {website} saved.")

    # تابع برای نمایش رمز عبور
    def get_password(self, website):
        if website in self.passwords:
            return self.passwords[website]
        else:
            return "Password for this site is not saved."

    # تابع برای حذف رمز عبور
    def delete_password(self, website):
        if website in self.passwords:
            del self.passwords[website]
            print(f"Password for {website} deleted.")
        else:
            print("This site is not in the system.")

# ایجاد شیء از سیستم مدیریت رمز عبور
manager = PasswordManager()

# منوی سیستم مدیریت رمز عبور
while True:
    print("\n1. Save password")
    print("2. Display password")
    print("3. Delete password")
    print("4. Exit")
    
    choice = input("Please select an option: ")
    
    if choice == "1":
        website = input("Enter the website name: ")
        password = input("Enter the password: ")
        manager.add_password(website, password)
    elif choice == "2":
        website = input("Enter the website name: ")
        print(f"Password for {website}: {manager.get_password(website)}")
    elif choice == "3":
        website = input("Enter the website name: ")
        manager.delete_password(website)
    elif choice == "4":
        print("Exiting the program...")
        break
