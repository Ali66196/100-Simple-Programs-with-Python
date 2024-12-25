# ذخیره و خواندن اطلاعات کاربر در یک فایل

# تابع برای ذخیره اطلاعات کاربر در فایل
def save_user_data(username, password):
    with open("user_data.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("User information saved successfully.")

# تابع برای خواندن اطلاعات کاربر از فایل
def read_user_data():
    try:
        with open("user_data.txt", "r") as file:
            data = file.readlines()
            print("Saved user data:")
            for line in data:
                print(line.strip())
    except FileNotFoundError:
        print("User data file not found.")

# منوی ذخیره و خواندن اطلاعات
while True:
    print("\n1. Save user data")
    print("2. Display user data")
    print("3. Exit")
    
    choice = input("Please select an option: ")
    
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        save_user_data(username, password)
    elif choice == "2":
        read_user_data()
    elif choice == "3":
        print("Exiting the program...")
        break
