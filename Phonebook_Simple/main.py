# ایجاد یک دفترچه تلفن ساده

# ایجاد یک دیکشنری برای ذخیره شماره تلفن‌ها
phonebook = {}

# تابعی برای اضافه کردن یک مخاطب
def add_contact(name, phone):
    phonebook[name] = phone

# تابعی برای نمایش دفترچه تلفن
def show_phonebook():
    if not phonebook:
        print("Phonebook is empty.")
    for name, phone in phonebook.items():
        print(f"{name}: {phone}")

# تابعی برای جستجو در دفترچه تلفن
def search_contact(name):
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print("Contact not found.")

# منوی ساده برای مدیریت دفترچه تلفن
while True:
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Show Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        add_contact(name, phone)
    elif choice == '2':
        show_phonebook()
    elif choice == '3':
        name = input("Enter the name to search: ")
        search_contact(name)
    elif choice == '4':
        break
    else:
        print("Invalid choice.")
